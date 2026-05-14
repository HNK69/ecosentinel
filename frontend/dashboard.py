"""
EcoSentinel — Dashboard Assembler
===================================
Combines CSS, JS, and HTML template into a single ESP32-compatible HTML string.
Exports get_html() for use by the Flask backend and ESP32 firmware.
"""

from frontend.styles import get_css
from frontend.scripts import get_js
from frontend.template import get_template


def get_html() -> str:
    """
    Returns a complete, self-contained HTML document for the EcoSentinel dashboard.
    
    - All CSS is inlined in a <style> tag
    - All JS is inlined in a <script> tag
    - No external dependencies except Google Fonts
    - Optimized for ESP32 webserver rendering
    """
    html = get_template()
    html = html.replace("{{CSS}}", get_css())
    html = html.replace("{{JS}}", get_js())
    return html
