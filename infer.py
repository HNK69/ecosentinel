"""
EcoSentinel — TFLite Inference Script
======================================
Runs inference on the exported INT8/float TFLite model.

Modes:
  1. File mode   : python infer.py --model ecosentinel_int8.tflite --audio sample.wav
  2. Folder mode : python infer.py --model ecosentinel_int8.tflite --audio ./test_clips/
  3. Mic mode    : python infer.py --model ecosentinel_int8.tflite --mic

Requirements:
    pip install tensorflow numpy librosa sounddevice scipy
"""

import argparse
import sys
import time
from pathlib import Path
from typing import List, Optional, Tuple

import numpy as np

# ─────────────────────────────────────────────────
# CONFIGURATION — must match training exactly
# ─────────────────────────────────────────────────

SAMPLE_RATE       = 16000
CLIP_DURATION     = 3.0
CLIP_SAMPLES      = int(SAMPLE_RATE * CLIP_DURATION)   # 48000
HOP_SAMPLES       = int(SAMPLE_RATE * 1.5)             # 50% overlap
SILENCE_THRESHOLD = 0.01

# MFCC parameters — identical to features.py
N_MFCC      = 40
N_FFT       = 512
HOP_LENGTH  = 160
WIN_LENGTH  = 400
N_MELS      = 64
FMIN        = 50
FMAX        = 8000
FRAMES      = 300   # fixed time axis after pad/trim

CLASS_NAMES = ["chainsaw", "excavator", "forest", "mining", "noise", "tractor"]

# Visual config
BAR_WIDTH   = 40
COLORS = {
    "chainsaw":  "\033[91m",   # red
    "excavator": "\033[93m",   # yellow
    "forest":    "\033[92m",   # green
    "mining":    "\033[95m",   # magenta
    "noise":     "\033[90m",   # grey
    "tractor":   "\033[94m",   # blue
    "reset":     "\033[0m",
    "bold":      "\033[1m",
    "dim":       "\033[2m",
}

ALERT_CLASSES = {"chainsaw", "excavator", "mining", "tractor"}


# ─────────────────────────────────────────────────
# AUDIO UTILITIES
# ─────────────────────────────────────────────────

def load_audio(path: Path) -> Optional[np.ndarray]:
    """Load any audio file → mono float32 at 16kHz."""
    try:
        import librosa
        samples, _ = librosa.load(str(path), sr=SAMPLE_RATE, mono=True)
        return samples.astype(np.float32)
    except Exception as e:
        print(f"  [ERROR] Could not load {path.name}: {e}")
        return None


def normalize(samples: np.ndarray) -> np.ndarray:
    peak = np.max(np.abs(samples))
    return samples / peak if peak > 1e-9 else samples


def pad_or_trim(arr: np.ndarray, length: int) -> np.ndarray:
    if len(arr) >= length:
        return arr[:length]
    return np.pad(arr, (0, length - len(arr)))


def is_silent(clip: np.ndarray) -> bool:
    return float(np.sqrt(np.mean(clip ** 2))) < SILENCE_THRESHOLD


def slice_into_clips(samples: np.ndarray) -> List[np.ndarray]:
    """Sliding window → list of 3-second float32 clips."""
    clips = []
    start = 0
    while start < len(samples):
        clip = pad_or_trim(samples[start : start + CLIP_SAMPLES], CLIP_SAMPLES)
        if not is_silent(clip):
            clips.append(normalize(clip))
        start += HOP_SAMPLES
    return clips


# ─────────────────────────────────────────────────
# MFCC FEATURE EXTRACTION
# ─────────────────────────────────────────────────

def extract_mfcc(samples: np.ndarray) -> np.ndarray:
    """
    Extract MFCC features identical to training pipeline.
    Returns shape (1, 40, 300, 1) — ready for TFLite input tensor.
    """
    import librosa

    mfcc = librosa.feature.mfcc(
        y=samples,
        sr=SAMPLE_RATE,
        n_mfcc=N_MFCC,
        n_fft=N_FFT,
        hop_length=HOP_LENGTH,
        win_length=WIN_LENGTH,
        n_mels=N_MELS,
        fmin=FMIN,
        fmax=FMAX,
        center=False,
    )  # → (40, variable_frames)
    mfcc = mfcc[:40, :]
    print("MFCC raw shape:", mfcc.shape)

    # Fix time axis to exactly FRAMES
    if mfcc.shape[1] < FRAMES:
        pad_width = FRAMES - mfcc.shape[1]
        mfcc = np.pad(mfcc, ((0, 0), (0, pad_width)))
    else:
        mfcc = mfcc[:, :FRAMES]

    # Z-score normalize (same as training)
    mfcc = (mfcc - mfcc.mean()) / (mfcc.std() + 1e-8)

    # Add batch + channel dims → (1, 40, 300, 1)
    return mfcc[np.newaxis, ..., np.newaxis].astype(np.float32)


# ─────────────────────────────────────────────────
# TFLITE INTERPRETER
# ─────────────────────────────────────────────────

class EcoSentinelInterpreter:
    """Thin wrapper around TFLite Interpreter for EcoSentinel inference."""

    def __init__(self, model_path: str):
        try:
            # Try ai_edge_litert first, then tflite_runtime, then full TF
            try:
                from ai_edge_litert.interpreter import Interpreter
                self.interpreter = Interpreter(model_path=model_path)
            except ImportError:
                try:
                    import tflite_runtime.interpreter as tflite
                    self.interpreter = tflite.Interpreter(model_path=model_path)
                except ImportError:
                    import tensorflow as tf
                    self.interpreter = tf.lite.Interpreter(model_path=model_path)

            self.interpreter.allocate_tensors()
            self.input_details  = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()

            in_shape  = self.input_details[0]["shape"].tolist()
            out_shape = self.output_details[0]["shape"].tolist()
            print(f"  Model loaded   : {model_path}")
            print(f"  Input  shape   : {in_shape}")
            print(f"  Output shape   : {out_shape}")
            print(f"  Input  dtype   : {self.input_details[0]['dtype'].__name__}")

        except Exception as e:
            sys.exit(f"[FATAL] Could not load model '{model_path}': {e}")

    def predict(self, feature: np.ndarray) -> np.ndarray:
        """
        Run one inference pass.

        Args:
            feature: shape (1, 40, 300, 1), float32
        Returns:
            probabilities: shape (num_classes,)
        """
        print("Feature shape:", feature.shape)
        self.interpreter.set_tensor(self.input_details[0]["index"], feature)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(self.output_details[0]["index"])
        return output[0]  # (num_classes,)

    def predict_clip(self, samples: np.ndarray) -> Tuple[str, float, np.ndarray]:
        """
        Full pipeline: raw samples → predicted class + confidence.

        Returns:
            (class_name, confidence, all_probabilities)
        """
        feature = extract_mfcc(samples)
        probs   = self.predict(feature)
        idx     = int(np.argmax(probs))
        return CLASS_NAMES[idx], float(probs[idx]), probs


# ─────────────────────────────────────────────────
# DISPLAY
# ─────────────────────────────────────────────────

def confidence_bar(prob: float, width: int = BAR_WIDTH) -> str:
    filled = int(prob * width)
    return "█" * filled + "░" * (width - filled)


def print_prediction_table(probs: np.ndarray, predicted: str, confidence: float) -> None:
    """Print a formatted confidence table with color-coded bars."""
    c = COLORS
    print()
    print(f"  {'CLASS':<12}  {'CONFIDENCE':>8}   {'BAR'}")
    print(f"  {'─'*12}  {'─'*8}   {'─'*BAR_WIDTH}")

    sorted_idx = np.argsort(probs)[::-1]
    for idx in sorted_idx:
        name  = CLASS_NAMES[idx]
        prob  = float(probs[idx])
        bar   = confidence_bar(prob)
        color = COLORS.get(name, "")
        bold  = c["bold"] if name == predicted else ""
        mark  = " ◄" if name == predicted else ""
        print(f"  {bold}{color}{name:<12}{c['reset']}  {prob:>7.1%}   {color}{bar}{c['reset']}{mark}")

    print()
    alert = "🚨 ALERT — ILLEGAL ACTIVITY DETECTED" if predicted in ALERT_CLASSES else "✅ SAFE — Natural/Background Sound"
    color = c["bold"] + "\033[91m" if predicted in ALERT_CLASSES else c["bold"] + "\033[92m"
    print(f"  {color}Prediction : {predicted.upper()}  ({confidence:.1%}){c['reset']}")
    print(f"  {color}{alert}{c['reset']}")
    print()


def print_clip_summary(clip_results: list) -> None:
    """Aggregate predictions across multiple clips and print a summary."""
    if not clip_results:
        return

    # Majority vote + average confidence
    votes = {}
    for cls, conf, _ in clip_results:
        votes[cls] = votes.get(cls, [])
        votes[cls].append(conf)

    # Weighted by average confidence
    best_class = max(votes, key=lambda k: sum(votes[k]) / len(votes[k]))
    avg_conf   = sum(votes[best_class]) / len(votes[best_class])

    c = COLORS
    print(f"\n  {'═'*55}")
    print(f"  {c['bold']}  AGGREGATED RESULT  ({len(clip_results)} clips){c['reset']}")
    print(f"  {'═'*55}")
    for cls, confs in sorted(votes.items(), key=lambda x: -sum(x[1])/len(x[1])):
        avg = sum(confs) / len(confs)
        cnt = len(confs)
        print(f"  {c['bold'] if cls == best_class else ''}{cls:<12}{c['reset']}  "
              f"{avg:>6.1%} avg  ({cnt} clip{'s' if cnt>1 else ''})")
    print(f"\n  {c['bold']}Final: {best_class.upper()}  ({avg_conf:.1%} avg confidence){c['reset']}")
    print(f"  {'═'*55}\n")


# ─────────────────────────────────────────────────
# MODE 1: FILE INFERENCE
# ─────────────────────────────────────────────────

def infer_file(interpreter: EcoSentinelInterpreter, audio_path: Path) -> None:
    """Run inference on a single audio file."""
    print(f"\n{'═'*60}")
    print(f"  FILE: {audio_path.name}")
    print(f"{'═'*60}")

    samples = load_audio(audio_path)
    if samples is None:
        return

    duration = len(samples) / SAMPLE_RATE
    print(f"  Duration       : {duration:.1f}s")

    clips = slice_into_clips(samples)
    print(f"  Clips extracted: {len(clips)}")

    if not clips:
        print("  [WARN] No usable clips found (audio may be silent).")
        return

    clip_results = []
    for i, clip in enumerate(clips):
        t0 = time.perf_counter()
        cls, conf, probs = interpreter.predict_clip(clip)
        latency = (time.perf_counter() - t0) * 1000

        print(f"\n  ── Clip {i+1}/{len(clips)}  (latency: {latency:.1f}ms) ──")
        print_prediction_table(probs, cls, conf)
        clip_results.append((cls, conf, probs))

    if len(clips) > 1:
        print_clip_summary(clip_results)


def infer_folder(interpreter: EcoSentinelInterpreter, folder: Path) -> None:
    """Run inference on all audio files in a folder."""
    supported = {".wav", ".mp3", ".flac", ".ogg"}
    audio_files = [f for f in sorted(folder.iterdir())
                   if f.suffix.lower() in supported]

    if not audio_files:
        print(f"[ERROR] No audio files found in {folder}")
        return

    print(f"\nFound {len(audio_files)} audio files in {folder}\n")
    for path in audio_files:
        infer_file(interpreter, path)


# ─────────────────────────────────────────────────
# MODE 2: LIVE MICROPHONE INFERENCE
# ─────────────────────────────────────────────────

def infer_microphone(
    interpreter: EcoSentinelInterpreter,
    device: Optional[int] = None,
    confidence_threshold: float = 0.50,
) -> None:
    """
    Continuous real-time inference from microphone.

    Captures 3-second windows, runs inference, prints prediction.
    Press Ctrl+C to stop.
    """
    try:
        import sounddevice as sd
    except ImportError:
        sys.exit("[ERROR] sounddevice not installed. Run: pip install sounddevice")

    print(f"\n{'═'*60}")
    print(f"  🎙  LIVE MICROPHONE MODE")
    print(f"{'═'*60}")
    print(f"  Sample rate    : {SAMPLE_RATE} Hz")
    print(f"  Window size    : {CLIP_DURATION:.0f}s")
    print(f"  Threshold      : {confidence_threshold:.0%}")
    print(f"  Press Ctrl+C to stop\n")

    # List available devices
    if device is None:
        print("  Available input devices:")
        devices = sd.query_devices()
        for i, d in enumerate(devices):
            if d["max_input_channels"] > 0:
                print(f"    [{i}] {d['name']}")
        print()

    window_count = 0
    c = COLORS

    try:
        while True:
            window_count += 1
            print(f"  {c['dim']}[{window_count:04d}] Listening for {CLIP_DURATION:.0f}s...{c['reset']}", end="\r")

            # Capture audio
            try:
                recording = sd.rec(
                    frames=CLIP_SAMPLES,
                    samplerate=SAMPLE_RATE,
                    channels=1,
                    dtype="float32",
                    device=device,
                    blocking=True,
                )
            except Exception as e:
                print(f"\n  [ERROR] Microphone capture failed: {e}")
                time.sleep(1)
                continue

            clip = recording[:, 0]  # (48000,)

            if is_silent(clip):
                print(f"  {c['dim']}[{window_count:04d}] Silence — skipping{c['reset']}      ", end="\r")
                continue

            clip = normalize(clip)

            # Inference
            t0 = time.perf_counter()
            cls, conf, probs = interpreter.predict_clip(clip)
            latency = (time.perf_counter() - t0) * 1000

            # Only print if above threshold
            if conf < confidence_threshold:
                print(f"  {c['dim']}[{window_count:04d}] Low confidence ({conf:.1%}) — skipping{c['reset']}      ",
                      end="\r")
                continue

            # Clear line and print result
            print(" " * 60, end="\r")
            timestamp = time.strftime("%H:%M:%S")
            color = c["bold"] + "\033[91m" if cls in ALERT_CLASSES else c["bold"] + "\033[92m"
            alert = "🚨" if cls in ALERT_CLASSES else "✅"

            print(f"  [{timestamp}]  {alert}  {color}{cls.upper():<12}{c['reset']}  "
                  f"{conf:>6.1%}  ({latency:.0f}ms)")

            # Print full table every 5 windows or on alert
            if cls in ALERT_CLASSES or window_count % 5 == 0:
                print_prediction_table(probs, cls, conf)

    except KeyboardInterrupt:
        print(f"\n\n  Microphone inference stopped after {window_count} windows.")


# ─────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="EcoSentinel — TFLite Inference",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single file
  python infer.py --model models/ecosentinel_int8.tflite --audio test.wav

  # Folder of files
  python infer.py --model models/ecosentinel_int8.tflite --audio ./test_clips/

  # Live microphone
  python infer.py --model models/ecosentinel_int8.tflite --mic

  # Live mic with specific device and threshold
  python infer.py --model models/ecosentinel_int8.tflite --mic --device 1 --threshold 0.65
        """,
    )
    p.add_argument(
        "--model", "-m",
        type=str,
        required=True,
        help="Path to .tflite model file",
    )
    p.add_argument(
        "--audio", "-a",
        type=str,
        default=None,
        help="Path to audio file or folder",
    )
    p.add_argument(
        "--mic",
        action="store_true",
        help="Enable live microphone inference",
    )
    p.add_argument(
        "--device", "-d",
        type=int,
        default=None,
        help="Microphone device index (run without --device to list options)",
    )
    p.add_argument(
        "--threshold", "-t",
        type=float,
        default=0.50,
        help="Minimum confidence to print mic predictions (default: 0.50)",
    )
    p.add_argument(
        "--classes",
        type=str,
        nargs="+",
        default=None,
        help="Override class names (must match model output order)",
    )
    return p.parse_args()


# ─────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────

def main() -> None:
    args = parse_args()

    # Override class names if provided
    if args.classes:
        global CLASS_NAMES
        CLASS_NAMES = args.classes
        print(f"  Class names overridden: {CLASS_NAMES}")

    # Validate model path
    model_path = Path(args.model)
    if not model_path.exists():
        sys.exit(f"[ERROR] Model not found: {model_path}")

    # Print header
    print(f"\n{'═'*60}")
    print(f"  🌿  EcoSentinel — Environmental Sound Classifier")
    print(f"{'═'*60}")
    print(f"  Model          : {model_path.name}")
    print(f"  Classes        : {', '.join(CLASS_NAMES)}")
    print(f"  Alert classes  : {', '.join(ALERT_CLASSES)}")

    # Load interpreter
    interpreter = EcoSentinelInterpreter(str(model_path))

    # Route to correct mode
    if args.mic:
        infer_microphone(interpreter, device=args.device,
                         confidence_threshold=args.threshold)

    elif args.audio:
        audio_path = Path(args.audio)
        if audio_path.is_dir():
            infer_folder(interpreter, audio_path)
        elif audio_path.is_file():
            infer_file(interpreter, audio_path)
        else:
            sys.exit(f"[ERROR] Audio path not found: {audio_path}")

    else:
        print("\n[ERROR] Provide --audio <file/folder> or --mic\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
