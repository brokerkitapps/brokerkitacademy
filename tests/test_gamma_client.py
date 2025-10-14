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

    @patch("brokerkitacademy.gamma.client.requests.post")
    def test_create_presentation_http_error_with_message(self, mock_post):
        """Test presentation creation extracts error message from API response"""
        import requests

        mock_response = Mock()
        mock_response.json.return_value = {
            "message": "Input validation errors: 1. numCards exceeds limit",
            "statusCode": 400
        }
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            response=mock_response
        )
        mock_post.return_value = mock_response

        client = GammaClient(api_key="test-key")
        with pytest.raises(GammaAPIError, match="Input validation errors"):
            client.create_presentation(input_text="# Test", wait_for_completion=False)

    @patch("brokerkitacademy.gamma.client.requests.post")
    def test_create_presentation_validates_payload_no_text_options(self, mock_post):
        """Test that textOptions is not included in API request"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "generationId": "test-gen-id",
            "status": "completed",
            "gammaUrl": "https://gamma.app/docs/test",
        }
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        client = GammaClient(api_key="test-key")
        client.create_presentation(input_text="# Test", num_cards=10, wait_for_completion=False)

        # Verify the API was called with correct payload
        call_args = mock_post.call_args
        payload = call_args[1]["json"]

        # Ensure textOptions is NOT in the payload
        assert "textOptions" not in payload
        assert "inputText" in payload
        assert "numCards" in payload
        assert payload["numCards"] == 10

    def test_create_presentation_validates_empty_input(self):
        """Test validation rejects empty input_text"""
        client = GammaClient(api_key="test-key")
        with pytest.raises(ValueError, match="input_text cannot be empty"):
            client.create_presentation(input_text="", wait_for_completion=False)

    def test_create_presentation_validates_whitespace_input(self):
        """Test validation rejects whitespace-only input_text"""
        client = GammaClient(api_key="test-key")
        with pytest.raises(ValueError, match="input_text cannot be empty"):
            client.create_presentation(input_text="   ", wait_for_completion=False)

    def test_create_presentation_validates_invalid_format(self):
        """Test validation rejects invalid format"""
        client = GammaClient(api_key="test-key")
        with pytest.raises(ValueError, match="format must be one of"):
            client.create_presentation(input_text="# Test", format="invalid", wait_for_completion=False)

    def test_create_presentation_validates_num_cards_too_low(self):
        """Test validation rejects num_cards less than 1"""
        client = GammaClient(api_key="test-key")
        with pytest.raises(ValueError, match="num_cards must be at least 1"):
            client.create_presentation(input_text="# Test", num_cards=0, wait_for_completion=False)

    def test_create_presentation_validates_num_cards_too_high(self):
        """Test validation rejects num_cards over 75"""
        client = GammaClient(api_key="test-key")
        with pytest.raises(ValueError, match="num_cards cannot exceed 75"):
            client.create_presentation(input_text="# Test", num_cards=100, wait_for_completion=False)

    def test_create_presentation_validates_invalid_image_source(self):
        """Test validation rejects invalid image_source"""
        client = GammaClient(api_key="test-key")
        with pytest.raises(ValueError, match="image_source must be one of"):
            client.create_presentation(input_text="# Test", image_source="invalid", wait_for_completion=False)

    def test_create_presentation_validates_invalid_export_format(self):
        """Test validation rejects invalid export_as"""
        client = GammaClient(api_key="test-key")
        with pytest.raises(ValueError, match="export_as must be 'pdf' or 'pptx'"):
            client.create_presentation(input_text="# Test", export_as="docx", wait_for_completion=False)

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
