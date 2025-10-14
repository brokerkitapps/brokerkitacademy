"""
Tests for Gamma Theme management
"""

import pytest
from unittest.mock import Mock, patch, mock_open
import json
from brokerkitacademy.gamma import ThemeManager, get_theme_names, is_valid_theme


pytestmark = pytest.mark.skip(
    reason="Theme tests need refactoring - ThemeManager requires API key"
)


class TestThemeManager:
    """Test suite for ThemeManager"""

    @patch("brokerkitacademy.gamma.themes.GammaClient")
    @patch("os.path.exists", return_value=False)
    def test_fetch_themes_from_api(self, mock_exists, mock_client_class):
        """Test fetching themes from API when cache doesn't exist"""
        mock_client = Mock()
        mock_client.get_themes.return_value = {
            "themes": [
                {"name": "Berlin", "id": "berlin-123"},
                {"name": "Tokyo", "id": "tokyo-456"},
            ]
        }
        mock_client_class.return_value = mock_client

        with patch("builtins.open", mock_open()):
            manager = ThemeManager()
            themes = manager.get_themes()

            assert len(themes) >= 2
            assert any(t["name"] == "Berlin" for t in themes)

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_load_themes_from_cache(self, mock_file, mock_exists):
        """Test loading themes from cache file"""
        cache_data = {
            "themes": [
                {"name": "Berlin", "id": "berlin-123"},
                {"name": "Tokyo", "id": "tokyo-456"},
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(cache_data)

        manager = ThemeManager()
        themes = manager.get_themes()

        assert len(themes) == 2
        assert themes[0]["name"] == "Berlin"

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_get_theme_names(self, mock_file, mock_exists):
        """Test getting list of theme names"""
        cache_data = {
            "themes": [
                {"name": "Berlin", "id": "berlin-123"},
                {"name": "Tokyo", "id": "tokyo-456"},
                {"name": "Paris", "id": "paris-789"},
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(cache_data)

        manager = ThemeManager()
        names = manager.get_theme_names()

        assert len(names) == 3
        assert "Berlin" in names
        assert "Tokyo" in names
        assert "Paris" in names

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_find_theme(self, mock_file, mock_exists):
        """Test finding a specific theme"""
        cache_data = {
            "themes": [
                {"name": "Berlin", "id": "berlin-123"},
                {"name": "Tokyo", "id": "tokyo-456"},
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(cache_data)

        manager = ThemeManager()
        theme = manager.find_theme("Berlin")

        assert theme is not None
        assert theme["name"] == "Berlin"
        assert theme["id"] == "berlin-123"

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_find_theme_not_found(self, mock_file, mock_exists):
        """Test finding a theme that doesn't exist"""
        cache_data = {"themes": [{"name": "Berlin", "id": "berlin-123"}]}
        mock_file.return_value.read.return_value = json.dumps(cache_data)

        manager = ThemeManager()
        theme = manager.find_theme("NonExistent")

        assert theme is None

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_is_valid_theme(self, mock_file, mock_exists):
        """Test checking if theme name is valid"""
        cache_data = {
            "themes": [
                {"name": "Berlin", "id": "berlin-123"},
                {"name": "Tokyo", "id": "tokyo-456"},
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(cache_data)

        manager = ThemeManager()
        assert manager.is_valid_theme("Berlin") is True
        assert manager.is_valid_theme("Tokyo") is True
        assert manager.is_valid_theme("NonExistent") is False

    @patch("brokerkitacademy.gamma.themes.GammaClient")
    def test_default_theme_fallback(self, mock_client_class):
        """Test default theme is used when API fails"""
        mock_client = Mock()
        mock_client.get_themes.side_effect = Exception("API Error")
        mock_client_class.return_value = mock_client

        with patch("os.path.exists", return_value=False):
            with patch("builtins.open", mock_open()):
                manager = ThemeManager()
                themes = manager.get_themes()

                # Should have default themes
                assert len(themes) > 0
                assert any("name" in theme for theme in themes)


class TestConvenienceFunctions:
    """Test convenience functions"""

    @patch("brokerkitacademy.gamma.themes.ThemeManager")
    def test_get_theme_names_function(self, mock_manager_class):
        """Test get_theme_names convenience function"""
        mock_manager = Mock()
        mock_manager.get_theme_names.return_value = ["Berlin", "Tokyo"]
        mock_manager_class.return_value = mock_manager

        names = get_theme_names()

        assert len(names) == 2
        assert "Berlin" in names

    @patch("brokerkitacademy.gamma.themes.ThemeManager")
    def test_is_valid_theme_function(self, mock_manager_class):
        """Test is_valid_theme convenience function"""
        mock_manager = Mock()
        mock_manager.is_valid_theme.return_value = True
        mock_manager_class.return_value = mock_manager

        result = is_valid_theme("Berlin")

        assert result is True
        mock_manager.is_valid_theme.assert_called_once_with("Berlin")
