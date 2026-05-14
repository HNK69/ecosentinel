"""
EcoSentinel — Flask Backend Application
=========================================
Production-ready REST API for Edge-AI environmental audio inference.

Endpoints:
    POST /predict        — Upload audio file, get TFLite inference result
    GET  /health         — Health check
    GET  /               — ESP32-compatible integrated dashboard
    GET  /api/status     — System status for dashboard live updates
"""

import os
import sys
import uuid
import time
import traceback
from pathlib import Path
from datetime import datetime, timezone

from flask import Flask, request, jsonify, Response
from flask_cors import CORS

# ─────────────────────────────────────────────────
# Ensure project root is importable
# ─────────────────────────────────────────────────
PROJECT_ROOT = str(Path(__file__).resolve().parent.parent)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.config import (
    HOST, PORT, DEBUG,
    UPLOAD_DIR, ALLOWED_EXTENSIONS, MAX_CONTENT_LENGTH,
    THREAT_CLASSES,
)
from backend.utils.logger import setup_logger
from backend.utils.cleanup import start_cleanup_scheduler, cleanup_uploads
from backend.models.engine import InferenceEngine
from frontend import get_landing_html, get_dashboard_html

# ─────────────────────────────────────────────────
# APPLICATION FACTORY
# ─────────────────────────────────────────────────

logger = setup_logger()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
CORS(app, resources={r"/*": {"origins": "*"}})

# Create upload directory
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize inference engine
engine = InferenceEngine(logger=logger)

# Track system state for dashboard
_system_state = {
    "boot_time": datetime.now(timezone.utc).isoformat(),
    "total_predictions": 0,
    "total_threats": 0,
    "last_prediction": None,
    "uptime_start": time.time(),
}


def _allowed_file(filename: str) -> bool:
    """Check if uploaded file has an allowed extension."""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


# ─────────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────────

@app.route("/", methods=["GET"])
def index():
    """Serve the landing page."""
    return Response(get_landing_html(), mimetype="text/html")


@app.route("/dashboard", methods=["GET"])
@app.route("/dashboard/", methods=["GET"])
def dashboard_view():
    """Serve the monitoring dashboard."""
    return Response(get_dashboard_html(), mimetype="text/html")


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    uptime = time.time() - _system_state["uptime_start"]
    return jsonify({
        "status": "operational",
        "service": "EcoSentinel Inference Server",
        "model_loaded": engine.is_ready,
        "uptime_seconds": round(uptime, 1),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/api/status", methods=["GET"])
def api_status():
    """System status for live dashboard updates."""
    uptime = time.time() - _system_state["uptime_start"]
    return jsonify({
        "status": "operational",
        "model_loaded": engine.is_ready,
        "uptime_seconds": round(uptime, 1),
        "total_predictions": _system_state["total_predictions"],
        "total_threats": _system_state["total_threats"],
        "last_prediction": _system_state["last_prediction"],
        "boot_time": _system_state["boot_time"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/predict", methods=["POST"])
def predict():
    """
    Run TFLite inference on uploaded audio.

    Input:  multipart/form-data with 'audio' file field
    Output: JSON with predicted_class, confidence, is_threat, all_scores
    """
    request_id = str(uuid.uuid4())[:8]
    logger.info("[%s] Prediction request received", request_id)

    # ── Validate request ──
    if "audio" not in request.files:
        logger.warning("[%s] No 'audio' field in request", request_id)
        return jsonify({
            "error": "No audio file provided",
            "detail": "Include an 'audio' field in multipart/form-data",
        }), 400

    audio_file = request.files["audio"]

    if audio_file.filename == "":
        logger.warning("[%s] Empty filename", request_id)
        return jsonify({"error": "Empty filename"}), 400

    if not _allowed_file(audio_file.filename):
        logger.warning("[%s] Unsupported format: %s", request_id, audio_file.filename)
        return jsonify({
            "error": "Unsupported audio format",
            "allowed": list(ALLOWED_EXTENSIONS),
        }), 400

    # ── Save temporary file ──
    ext = Path(audio_file.filename).suffix.lower()
    temp_filename = f"{request_id}_{int(time.time())}{ext}"
    temp_path = os.path.join(UPLOAD_DIR, temp_filename)

    try:
        audio_file.save(temp_path)
        file_size = os.path.getsize(temp_path)
        logger.info("[%s] Saved upload: %s (%d bytes)", request_id, temp_filename, file_size)
    except Exception as e:
        logger.error("[%s] Failed to save upload: %s", request_id, e)
        return jsonify({"error": "Failed to save audio file"}), 500

    # ── Run inference ──
    try:
        t0 = time.perf_counter()
        result = engine.predict_file(temp_path)
        latency_ms = (time.perf_counter() - t0) * 1000

        result["request_id"] = request_id
        result["inference_latency_ms"] = round(latency_ms, 1)

        # Update system state
        _system_state["total_predictions"] += 1
        if result.get("is_threat"):
            _system_state["total_threats"] += 1
        _system_state["last_prediction"] = result

        logger.info(
            "[%s] Inference complete in %.1fms — %s (%.1f%%)",
            request_id,
            latency_ms,
            result["predicted_class"],
            result["confidence"] * 100,
        )

        return jsonify(result)

    except ValueError as e:
        logger.error("[%s] Audio processing error: %s", request_id, e)
        return jsonify({"error": str(e)}), 422

    except Exception as e:
        logger.error("[%s] Inference failed: %s\n%s", request_id, e, traceback.format_exc())
        return jsonify({"error": "Inference failed", "detail": str(e)}), 500

    finally:
        # Cleanup temp file immediately
        try:
            if os.path.exists(temp_path):
                os.remove(temp_path)
                logger.debug("[%s] Temp file removed: %s", request_id, temp_filename)
        except OSError:
            pass


# ─────────────────────────────────────────────────
# ERROR HANDLERS
# ─────────────────────────────────────────────────

@app.errorhandler(413)
def too_large(e):
    return jsonify({
        "error": "File too large",
        "max_size_mb": MAX_CONTENT_LENGTH // (1024 * 1024),
    }), 413


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500


# ─────────────────────────────────────────────────
# STARTUP
# ─────────────────────────────────────────────────

def create_app():
    """Application factory for production deployment."""
    engine.initialize()
    start_cleanup_scheduler(logger)
    logger.info("EcoSentinel server ready — http://%s:%d", HOST, PORT)
    return app


if __name__ == "__main__":
    create_app()
    app.run(host=HOST, port=PORT, debug=DEBUG)
