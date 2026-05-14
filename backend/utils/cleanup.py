"""
EcoSentinel — File Cleanup Utility
====================================
Handles temporary upload cleanup on a background schedule.
"""

import os
import time
import threading
from pathlib import Path

from backend.config import UPLOAD_DIR, CLEANUP_INTERVAL_SECONDS, UPLOAD_MAX_AGE_SECONDS


def cleanup_uploads(logger=None) -> int:
    """
    Remove uploaded files older than UPLOAD_MAX_AGE_SECONDS.
    Returns number of files removed.
    """
    removed = 0
    upload_path = Path(UPLOAD_DIR)

    if not upload_path.exists():
        return 0

    now = time.time()
    for f in upload_path.iterdir():
        if f.is_file():
            age = now - f.stat().st_mtime
            if age > UPLOAD_MAX_AGE_SECONDS:
                try:
                    f.unlink()
                    removed += 1
                    if logger:
                        logger.debug("Cleaned up: %s (age: %.0fs)", f.name, age)
                except OSError as e:
                    if logger:
                        logger.warning("Failed to remove %s: %s", f.name, e)

    return removed


def start_cleanup_scheduler(logger=None):
    """Start a daemon thread that periodically cleans up old uploads."""

    def _worker():
        while True:
            time.sleep(CLEANUP_INTERVAL_SECONDS)
            try:
                count = cleanup_uploads(logger)
                if count > 0 and logger:
                    logger.info("Cleanup: removed %d stale upload(s)", count)
            except Exception as e:
                if logger:
                    logger.error("Cleanup error: %s", e)

    thread = threading.Thread(target=_worker, daemon=True, name="upload-cleanup")
    thread.start()
    if logger:
        logger.info(
            "Upload cleanup scheduler started (interval=%ds, max_age=%ds)",
            CLEANUP_INTERVAL_SECONDS,
            UPLOAD_MAX_AGE_SECONDS,
        )
