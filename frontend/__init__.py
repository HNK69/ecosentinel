"""
EcoSentinel — Integrated Frontend Module
==========================================
Exports get_landing_html() and get_dashboard_html() for Flask routing.
"""

from frontend.dashboard import get_landing_html, get_dashboard_html, get_html

__all__ = ["get_landing_html", "get_dashboard_html", "get_html"]
