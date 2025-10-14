"""
Tests for Gamma API Client
"""

import pytest
from unittest.mock import Mock, patch
from brokerkitacademy.gamma import GammaClient, GammaAPIError


class TestGammaClient:
    """Test suite for GammaClient"""

    def test_client_initialization_with_key(self):
        """Test client can be initialized with API key"""
        client = GammaClient(api_key="test-key")
        assert client.api_key == "test-key"

    def test_client_initialization_without_key_raises_error(self):
        """Test client raises error when no API key is provided"""
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="Gamma API key is required"):
                GammaClient()

    def test_client_initialization_from_env(self):
        """Test client reads API key from environment"""
        with patch.dict("os.environ", {"GAMMA_API_KEY": "env-test-key"}):
            client = GammaClient()
            assert client.api_key == "env-test-key"

    def test_get_headers(self):
        """Test API headers are correctly formatted"""
        client = GammaClient(api_key="test-key")
        headers = client._get_headers()
        assert headers["X-API-KEY"] == "test-key"
        assert headers["Content-Type"] == "application/json"

    @patch("brokerkitacademy.gamma.client.requests.post")
    def test_create_presentation_success(self, mock_post):
        """Test successful presentation creation"""
        # Mock successful API response
        mock_response = Mock()
        mock_response.json.return_value = {
            "generationId": "test-gen-id",
            "status": "completed",
            "gammaUrl": "https://gamma.app/docs/test",
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = GammaClient(api_key="test-key")
        result = client.create_presentation(
            input_text="# Test", num_cards=10, wait_for_completion=False
        )

        assert result["generationId"] == "test-gen-id"
        assert result["status"] == "completed"
        assert result["gammaUrl"] == "https://gamma.app/docs/test"

    @patch("brokerkitacademy.gamma.client.requests.post")
    def test_create_presentation_api_error(self, mock_post):
        """Test presentation creation handles API errors"""
        import requests

        mock_post.side_effect = requests.exceptions.RequestException("API Error")

        client = GammaClient(api_key="test-key")
        with pytest.raises(GammaAPIError, match="Failed to create presentation"):
            client.create_presentation(input_text="# Test", wait_for_completion=False)

    @patch("brokerkitacademy.gamma.client.requests.get")
    def test_get_generation_status(self, mock_get):
        """Test getting generation status"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "generationId": "test-id",
            "status": "completed",
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        client = GammaClient(api_key="test-key")
        status = client.get_generation_status("test-id")

        assert status["generationId"] == "test-id"
        assert status["status"] == "completed"

    @patch("brokerkitacademy.gamma.client.requests.get")
    def test_get_themes(self, mock_get):
        """Test getting available themes"""
        mock_response = Mock()
        mock_response.json.return_value = {"themes": ["Berlin", "Tokyo", "Paris"]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        client = GammaClient(api_key="test-key")
        themes = client.get_themes()

        assert "themes" in themes
        assert len(themes["themes"]) == 3


class TestQuickPresentation:
    """Test convenience function"""

    @patch("brokerkitacademy.gamma.client.GammaClient")
    def test_create_quick_presentation(self, mock_client_class):
        """Test quick presentation creation"""
        from brokerkitacademy.gamma import create_quick_presentation

        mock_client = Mock()
        mock_client.create_presentation.return_value = {
            "gammaUrl": "https://gamma.app/docs/test"
        }
        mock_client_class.return_value = mock_client

        url = create_quick_presentation("# Test", 10)
        assert url == "https://gamma.app/docs/test"

    @patch("brokerkitacademy.gamma.client.GammaClient")
    def test_create_quick_presentation_no_url(self, mock_client_class):
        """Test quick presentation raises error when no URL returned"""
        from brokerkitacademy.gamma import create_quick_presentation

        mock_client = Mock()
        mock_client.create_presentation.return_value = {}
        mock_client_class.return_value = mock_client

        with pytest.raises(GammaAPIError, match="No gamma URL returned"):
            create_quick_presentation("# Test", 10)
