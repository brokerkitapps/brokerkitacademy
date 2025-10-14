"""
Tests for Gamma Metadata tracking
"""

import json
from unittest.mock import Mock, patch, mock_open
from brokerkitacademy.gamma import (
    GammaMetadata,
    add_presentation_quick,
    find_presentation_quick,
)


class TestGammaMetadata:
    """Test suite for GammaMetadata"""

    @patch("pathlib.Path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='{"presentations": []}')
    def test_load_existing_metadata(self, mock_file, mock_exists):
        """Test loading existing metadata file"""
        metadata = GammaMetadata(metadata_file="/tmp/test_metadata.json")
        assert metadata.metadata["presentations"] == []

    @patch("pathlib.Path.exists", return_value=False)
    @patch("pathlib.Path.mkdir")
    def test_create_new_metadata_file(self, mock_mkdir, mock_exists):
        """Test creating new metadata file when none exists"""
        metadata = GammaMetadata(metadata_file="/tmp/test_metadata.json")
        assert metadata.metadata["presentations"] == []

    @patch("pathlib.Path.exists", return_value=False)
    @patch("pathlib.Path.mkdir")
    @patch("builtins.open", new_callable=mock_open)
    def test_add_presentation(self, mock_file, mock_mkdir, mock_exists):
        """Test adding a new presentation"""
        metadata = GammaMetadata(metadata_file="/tmp/test_metadata.json")
        slug = metadata.add_presentation(
            local_file="test.md",
            gamma_id="test-id",
            gamma_url="https://gamma.app/docs/test",
            title="Test Presentation",
        )

        assert len(metadata.metadata["presentations"]) == 1
        pres = metadata.metadata["presentations"][0]
        assert pres["local_file"] == "test.md"
        assert pres["gamma_id"] == "test-id"
        assert pres["title"] == "Test Presentation"
        assert slug == "test-presentation"

    @patch("pathlib.Path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_find_by_file(self, mock_file, mock_exists):
        """Test finding presentation by file path"""
        test_data = {
            "presentations": [
                {
                    "id": "test-1",
                    "local_file": "assets/slides/test.md",
                    "gamma_id": "gamma-123",
                    "gamma_url": "https://gamma.app/docs/test",
                    "title": "Test",
                }
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(test_data)

        metadata = GammaMetadata(metadata_file="/tmp/test_metadata.json")
        pres = metadata.find_presentation("assets/slides/test.md")

        assert pres is not None
        assert pres["title"] == "Test"
        assert pres["gamma_id"] == "gamma-123"

    @patch("pathlib.Path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_find_by_url(self, mock_file, mock_exists):
        """Test finding presentation by Gamma URL"""
        test_data = {
            "presentations": [
                {
                    "id": "test-1",
                    "local_file": "test.md",
                    "gamma_url": "https://gamma.app/docs/xyz123",
                    "title": "Test",
                }
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(test_data)

        metadata = GammaMetadata(metadata_file="/tmp/test_metadata.json")
        pres = metadata.find_presentation("https://gamma.app/docs/xyz123")

        assert pres is not None
        assert pres["title"] == "Test"

    @patch("pathlib.Path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_find_by_id(self, mock_file, mock_exists):
        """Test finding presentation by ID"""
        test_data = {
            "presentations": [
                {"id": "my-presentation", "local_file": "test.md", "title": "Test"}
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(test_data)

        metadata = GammaMetadata(metadata_file="/tmp/test_metadata.json")
        pres = metadata.find_presentation("my-presentation")

        assert pres is not None
        assert pres["title"] == "Test"

    @patch("pathlib.Path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_get_all_presentations(self, mock_file, mock_exists):
        """Test getting all presentations"""
        test_data = {
            "presentations": [
                {"id": "1", "title": "First"},
                {"id": "2", "title": "Second"},
            ]
        }
        mock_file.return_value.read.return_value = json.dumps(test_data)

        metadata = GammaMetadata(metadata_file="/tmp/test_metadata.json")
        all_pres = metadata.list_presentations()

        assert len(all_pres) == 2
        assert all_pres[0]["title"] == "First"
        assert all_pres[1]["title"] == "Second"


class TestConvenienceFunctions:
    """Test convenience functions"""

    @patch("brokerkitacademy.gamma.metadata.GammaMetadata")
    def test_add_presentation_quick(self, mock_metadata_class):
        """Test quick add presentation function"""
        mock_metadata = Mock()
        mock_metadata.add_presentation.return_value = "test-slug"
        mock_metadata_class.return_value = mock_metadata

        result = add_presentation_quick(
            local_file="test.md",
            gamma_id="test-id",
            gamma_url="https://gamma.app/docs/test",
            title="Test",
        )

        assert result == "test-slug"
        mock_metadata.add_presentation.assert_called_once()

    @patch("brokerkitacademy.gamma.metadata.GammaMetadata")
    def test_find_presentation_quick(self, mock_metadata_class):
        """Test quick find presentation function"""
        mock_metadata = Mock()
        mock_metadata.find_presentation.return_value = {"title": "Test"}
        mock_metadata_class.return_value = mock_metadata

        result = find_presentation_quick("test.md")

        assert result["title"] == "Test"
        mock_metadata.find_presentation.assert_called_once_with("test.md")
