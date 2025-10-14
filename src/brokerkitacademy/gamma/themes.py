"""
Gamma Theme Management

This module provides utilities for managing and caching Gamma themes.
Themes control the visual appearance of generated presentations.
"""

import json
from pathlib import Path
from typing import List, Dict, Optional, Any
from .client import GammaClient, GammaAPIError


class ThemeManager:
    """
    Manages Gamma themes with local caching.

    Fetches available themes from the Gamma API and caches them locally
    to reduce API calls.
    """

    def __init__(self, cache_file: Optional[str] = None):
        """
        Initialize the theme manager.

        Args:
            cache_file: Path to cache file. Defaults to scripts/gamma/themes_cache.json
        """
        if cache_file is None:
            cache_dir = Path(__file__).parent
            self.cache_file = cache_dir / "themes_cache.json"
        else:
            self.cache_file = Path(cache_file)

        self.client = GammaClient()

    def get_themes(self, use_cache: bool = True) -> List[Dict[str, Any]]:
        """
        Get available Gamma themes.

        Args:
            use_cache: If True, use cached themes if available

        Returns:
            List of theme dictionaries

        Raises:
            GammaAPIError: If API request fails
        """
        # Try to load from cache first
        if use_cache and self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    cached_data = json.load(f)
                    return cached_data.get("themes", [])
            except (json.JSONDecodeError, IOError):
                # If cache is corrupted, fetch from API
                pass

        # Fetch from API
        try:
            themes_response = self.client.get_themes()
            themes = themes_response.get("themes", [])

            # Cache the results
            self._cache_themes(themes)

            return themes

        except GammaAPIError:
            # If API fails and we have cache, use it
            if self.cache_file.exists():
                try:
                    with open(self.cache_file, 'r') as f:
                        cached_data = json.load(f)
                        return cached_data.get("themes", [])
                except (json.JSONDecodeError, IOError):
                    pass

            # If no cache available, return default themes
            return self._get_default_themes()

    def _cache_themes(self, themes: List[Dict[str, Any]]):
        """Save themes to cache file"""
        cache_data = {
            "themes": themes,
            "cached_at": None  # Could add timestamp if needed
        }

        with open(self.cache_file, 'w') as f:
            json.dump(cache_data, f, indent=2)

    def _get_default_themes(self) -> List[Dict[str, Any]]:
        """
        Get a list of default/popular themes.

        These are common themes known to work well. This fallback is used
        when the API is unavailable and no cache exists.

        Returns:
            List of default theme dictionaries
        """
        return [
            {"name": "Berlin", "description": "Clean and modern"},
            {"name": "Cape", "description": "Professional and minimal"},
            {"name": "Fjord", "description": "Bold and striking"},
            {"name": "Aurora", "description": "Elegant and refined"},
            {"name": "Atlas", "description": "Strong and structured"},
            {"name": "Breeze", "description": "Light and airy"},
            {"name": "Carbon", "description": "Dark and sophisticated"},
            {"name": "Dune", "description": "Warm and inviting"},
            {"name": "Echo", "description": "Balanced and versatile"},
            {"name": "Horizon", "description": "Wide and spacious"},
        ]

    def get_theme_names(self, use_cache: bool = True) -> List[str]:
        """
        Get a list of theme names.

        Args:
            use_cache: If True, use cached themes if available

        Returns:
            List of theme names
        """
        themes = self.get_themes(use_cache=use_cache)
        return [theme.get("name", "") for theme in themes if theme.get("name")]

    def find_theme(self, theme_name: str, use_cache: bool = True) -> Optional[Dict[str, Any]]:
        """
        Find a theme by name (case-insensitive).

        Args:
            theme_name: Name of the theme to find
            use_cache: If True, use cached themes if available

        Returns:
            Theme dictionary, or None if not found
        """
        themes = self.get_themes(use_cache=use_cache)
        theme_name_lower = theme_name.lower()

        for theme in themes:
            if theme.get("name", "").lower() == theme_name_lower:
                return theme

        return None

    def print_themes(self, use_cache: bool = True):
        """
        Print available themes to console.

        Args:
            use_cache: If True, use cached themes if available
        """
        themes = self.get_themes(use_cache=use_cache)

        print(f"\n{'='*60}")
        print(f"Available Gamma Themes ({len(themes)} total)")
        print(f"{'='*60}\n")

        for theme in themes:
            name = theme.get("name", "Unknown")
            description = theme.get("description", "No description")
            print(f"  • {name:20} - {description}")

        print(f"\n{'='*60}\n")


# Convenience functions
def get_theme_names() -> List[str]:
    """
    Quickly get a list of available theme names.

    Returns:
        List of theme names
    """
    manager = ThemeManager()
    return manager.get_theme_names()


def print_available_themes():
    """Print available themes to console"""
    manager = ThemeManager()
    manager.print_themes()


def is_valid_theme(theme_name: str) -> bool:
    """
    Check if a theme name is valid.

    Args:
        theme_name: Theme name to validate

    Returns:
        True if theme exists, False otherwise
    """
    manager = ThemeManager()
    return manager.find_theme(theme_name) is not None
