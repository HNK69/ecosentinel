"""
EcoSentinel — Configuration Module
===================================
Centralized configuration for the Flask backend.
"""

import os
from pathlib import Path

# ─────────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = str(BASE_DIR / "ecosentinel_int8.tflite")
LABEL_MAP_PATH = str(BASE_DIR / "label_map.json")
UPLOAD_DIR = str(BASE_DIR / "backend" / "uploads")
LOG_DIR = str(BASE_DIR / "backend" / "logs")

# ─────────────────────────────────────────────────
# SERVER
# ─────────────────────────────────────────────────

HOST = os.getenv("ECOSENTINEL_HOST", "0.0.0.0")
PORT = int(os.getenv("ECOSENTINEL_PORT", "5000"))
DEBUG = os.getenv("ECOSENTINEL_DEBUG", "false").lower() == "true"

# ─────────────────────────────────────────────────
# INFERENCE
# ─────────────────────────────────────────────────

THREAT_CLASSES = {"chainsaw", "excavator", "mining", "tractor"}
ALLOWED_EXTENSIONS = {".wav", ".mp3", ".flac", ".ogg", ".webm", ".m4a"}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

# ─────────────────────────────────────────────────
# CLEANUP
# ─────────────────────────────────────────────────

CLEANUP_INTERVAL_SECONDS = 300   # 5 minutes
UPLOAD_MAX_AGE_SECONDS = 600     # 10 minutes
