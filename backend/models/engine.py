"""
EcoSentinel — Inference Engine
===============================
Wraps the existing infer.py pipeline for use by the Flask backend.
Reuses extract_mfcc(), EcoSentinelInterpreter, and predict_clip() exactly as provided.
"""

import sys
import json
from pathlib import Path
from datetime import datetime, timezone

# ─────────────────────────────────────────────────
# Make sure the project root is importable
# ─────────────────────────────────────────────────
PROJECT_ROOT = str(Path(__file__).resolve().parent.parent.parent)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import DIRECTLY from the existing infer.py — no reimplementation
from infer import (
    EcoSentinelInterpreter,
    extract_mfcc,
    load_audio,
    normalize,
    pad_or_trim,
    is_silent,
    slice_into_clips,
    CLASS_NAMES,
    ALERT_CLASSES,
    CLIP_SAMPLES,
    SAMPLE_RATE,
)

from backend.config import MODEL_PATH, LABEL_MAP_PATH, THREAT_CLASSES


class InferenceEngine:
    """
    Production inference engine that wraps the existing EcoSentinel pipeline.
    Provides JSON-serializable prediction results for the Flask API.
    """

    def __init__(self, logger=None):
        self.logger = logger
        self._interpreter = None
        self._label_map = None

    def initialize(self):
        """Load model and label map. Call once at startup."""
        if self.logger:
            self.logger.info("Loading TFLite model from: %s", MODEL_PATH)

        self._interpreter = EcoSentinelInterpreter(MODEL_PATH)

        # Load label map
        try:
            with open(LABEL_MAP_PATH, "r") as f:
                self._label_map = json.load(f)
            if self.logger:
                self.logger.info("Label map loaded: %s", self._label_map)
        except Exception as e:
            if self.logger:
                self.logger.warning("Could not load label_map.json: %s — using defaults", e)
            self._label_map = {str(i): name for i, name in enumerate(CLASS_NAMES)}

        if self.logger:
            self.logger.info("Inference engine ready — %d classes", len(CLASS_NAMES))

    @property
    def is_ready(self) -> bool:
        return self._interpreter is not None

    def predict_file(self, file_path: str) -> dict:
        """
        Run full inference on an audio file.

        Uses the EXACT pipeline from infer.py:
        load_audio → slice_into_clips → normalize → extract_mfcc → predict

        Returns:
            dict with predicted_class, confidence, is_threat, timestamp, all_scores
        """
        if not self.is_ready:
            raise RuntimeError("Inference engine not initialized. Call initialize() first.")

        audio_path = Path(file_path)

        if self.logger:
            self.logger.info("Running inference on: %s", audio_path.name)

        # Step 1: Load audio (reuses infer.py load_audio)
        samples = load_audio(audio_path)
        if samples is None:
            raise ValueError(f"Could not load audio file: {audio_path.name}")

        duration = len(samples) / SAMPLE_RATE
        if self.logger:
            self.logger.debug("Audio duration: %.1fs, samples: %d", duration, len(samples))

        # Step 2: Slice into clips (reuses infer.py slice_into_clips)
        clips = slice_into_clips(samples)
        if not clips:
            # If all clips are silent, run on padded raw audio
            if self.logger:
                self.logger.warning("No non-silent clips — running on padded raw audio")
            clips = [normalize(pad_or_trim(samples, CLIP_SAMPLES))]

        if self.logger:
            self.logger.debug("Extracted %d clips", len(clips))

        # Step 3: Run prediction on each clip using predict_clip() from infer.py
        clip_results = []
        for clip in clips:
            cls_name, confidence, all_probs = self._interpreter.predict_clip(clip)
            clip_results.append((cls_name, confidence, all_probs))

        # Step 4: Aggregate — pick highest-confidence result
        best_result = max(clip_results, key=lambda r: r[1])
        predicted_class, confidence, all_probs = best_result

        # Step 5: Build response
        all_scores = {}
        for i, name in enumerate(CLASS_NAMES):
            all_scores[name] = round(float(all_probs[i]), 4)

        result = {
            "predicted_class": predicted_class,
            "confidence": round(confidence, 4),
            "is_threat": predicted_class in THREAT_CLASSES,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "all_scores": all_scores,
            "audio_duration_seconds": round(duration, 2),
            "clips_analyzed": len(clips),
        }

        if self.logger:
            threat_flag = "🚨 THREAT" if result["is_threat"] else "✅ SAFE"
            self.logger.info(
                "Prediction: %s | %s | confidence=%.2f%% | clips=%d",
                predicted_class.upper(),
                threat_flag,
                confidence * 100,
                len(clips),
            )

        return result
