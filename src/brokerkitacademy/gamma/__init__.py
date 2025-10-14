"""
Gamma API Integration

This module provides a complete Python interface for the Gamma Generate API,
enabling automated creation and management of presentations, documents, and
social media content.

Main components:
- GammaClient: Full-featured API client with polling and error handling
- GammaMetadata: Metadata tracking system for presentations
- ThemeManager: Theme management and caching

Usage:
    from brokerkitacademy.gamma import GammaClient, GammaMetadata

    client = GammaClient()
    result = client.create_presentation(
        input_text="# My Presentation",
        num_cards=15
    )
"""

from .client import GammaClient, GammaAPIError, create_quick_presentation
from .metadata import (
    GammaMetadata,
    add_presentation_quick,
    find_presentation_quick,
)
from .themes import ThemeManager, get_theme_names, is_valid_theme

__all__ = [
    # Client
    "GammaClient",
    "GammaAPIError",
    "create_quick_presentation",
    # Metadata
    "GammaMetadata",
    "add_presentation_quick",
    "find_presentation_quick",
    # Themes
    "ThemeManager",
    "get_theme_names",
    "is_valid_theme",
]

__version__ = "1.0.0"
