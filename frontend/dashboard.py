"""
EcoSentinel — Dashboard Assembler
===================================
Combines CSS, JS, and HTML templates into self-contained HTML strings.
Exports get_landing_html() and get_dashboard_html() for Flask routes.
"""

from frontend.styles import get_css, get_landing_css
from frontend.scripts import get_js
from frontend.template import get_landing_template, get_dashboard_template


def get_landing_html() -> str:
    """Returns the cinematic landing/home page HTML (served at /)."""
    html = get_landing_template()
    html = html.replace("{{LANDING_CSS}}", get_landing_css())
    return html


def get_dashboard_html() -> str:
    """Returns the dashboard page HTML (served at /dashboard)."""
    html = get_dashboard_template()
    html = html.replace("{{CSS}}", get_css())
    html = html.replace("{{JS}}", get_js())
    return html


# Backward compatibility
def get_html() -> str:
    return get_dashboard_html()
