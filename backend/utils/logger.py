"""
EcoSentinel — Logging Utility
==============================
Production-grade logging configuration with file rotation and console output.
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from backend.config import LOG_DIR


def setup_logger(name: str = "ecosentinel", level: int = logging.INFO) -> logging.Logger:
    """
    Configure and return a production logger with:
    - Console handler (INFO+)
    - Rotating file handler (DEBUG+)
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # ── Console Handler ──
    console = logging.StreamHandler()
    console.setLevel(level)
    console_fmt = logging.Formatter(
        "%(asctime)s │ %(levelname)-8s │ %(message)s",
        datefmt="%H:%M:%S",
    )
    console.setFormatter(console_fmt)
    logger.addHandler(console)

    # ── File Handler ──
    os.makedirs(LOG_DIR, exist_ok=True)
    log_file = Path(LOG_DIR) / "ecosentinel.log"

    file_handler = RotatingFileHandler(
        str(log_file),
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_fmt = logging.Formatter(
        "%(asctime)s │ %(levelname)-8s │ %(module)s:%(lineno)d │ %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(file_fmt)
    logger.addHandler(file_handler)

    logger.info("Logger initialized — %s", name)
    return logger
