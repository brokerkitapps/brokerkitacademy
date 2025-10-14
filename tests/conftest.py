"""
Pytest configuration and shared fixtures
"""

import pytest
import os
from unittest.mock import patch


@pytest.fixture
def mock_api_key():
    """Fixture to provide a mock API key"""
    return "test-api-key-12345"


@pytest.fixture
def mock_env_vars(mock_api_key):
    """Fixture to mock environment variables"""
    with patch.dict(os.environ, {"GAMMA_API_KEY": mock_api_key}):
        yield


@pytest.fixture
def sample_presentation_data():
    """Fixture providing sample presentation data"""
    return {
        "id": "test-presentation",
        "local_file": "assets/slides/test-presentation.md",
        "gamma_id": "gamma-test-123",
        "gamma_url": "https://gamma.app/docs/test123",
        "title": "Test Presentation",
        "format": "presentation",
        "num_cards": 15,
        "theme_name": "Berlin",
        "created_at": "2025-10-13T12:00:00Z",
        "updated_at": "2025-10-13T12:00:00Z",
    }


@pytest.fixture
def sample_theme_data():
    """Fixture providing sample theme data"""
    return {
        "themes": [
            {"name": "Berlin", "id": "berlin-123", "category": "Modern"},
            {"name": "Tokyo", "id": "tokyo-456", "category": "Elegant"},
            {"name": "Paris", "id": "paris-789", "category": "Classic"},
            {"name": "New York", "id": "newyork-101", "category": "Bold"},
        ]
    }
