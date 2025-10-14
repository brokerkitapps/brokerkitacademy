"""
Gamma Metadata Tracking

This module manages metadata for Gamma presentations, tracking the relationship
between local markdown files and their corresponding Gamma presentations.

The metadata is stored in a JSON file at assets/slides/gamma_metadata.json
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path


class GammaMetadata:
    """
    Manages metadata for Gamma presentations.

    Tracks the relationship between local content files and Gamma presentations,
    including creation dates, URLs, and generation IDs.
    """

    def __init__(self, metadata_file: Optional[str] = None):
        """
        Initialize the metadata manager.

        Args:
            metadata_file: Path to the metadata JSON file.
                          Defaults to assets/slides/gamma_metadata.json
        """
        if metadata_file is None:
            # Default to assets/slides/gamma_metadata.json relative to project root
            project_root = Path(__file__).parent.parent.parent
            self.metadata_file = project_root / "assets" / "slides" / "gamma_metadata.json"
        else:
            self.metadata_file = Path(metadata_file)

        # Ensure parent directory exists
        self.metadata_file.parent.mkdir(parents=True, exist_ok=True)

        # Load or initialize metadata
        self.metadata = self._load_metadata()

    def _load_metadata(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load metadata from JSON file"""
        if self.metadata_file.exists():
            try:
                with open(self.metadata_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                # If file is corrupted, start fresh
                return {"presentations": []}
        else:
            return {"presentations": []}

    def _save_metadata(self):
        """Save metadata to JSON file"""
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)

    def add_presentation(
        self,
        local_file: str,
        gamma_id: str,
        gamma_url: str,
        title: str,
        format: str = "presentation",
        num_cards: int = 15,
        theme_name: Optional[str] = None
    ) -> str:
        """
        Add a new presentation to the metadata.

        Args:
            local_file: Path to the local markdown file
            gamma_id: Gamma generation ID
            gamma_url: URL to view the Gamma presentation
            title: Presentation title
            format: Format type (presentation/document/social)
            num_cards: Number of slides/cards
            theme_name: Theme used for the presentation

        Returns:
            Generated presentation ID (slug)
        """
        # Generate a unique slug from the title
        slug = self._generate_slug(title)

        # Create timestamp
        timestamp = datetime.utcnow().isoformat() + "Z"

        # Create presentation entry
        presentation = {
            "id": slug,
            "local_file": local_file,
            "gamma_id": gamma_id,
            "gamma_url": gamma_url,
            "created_at": timestamp,
            "updated_at": timestamp,
            "title": title,
            "format": format,
            "num_cards": num_cards
        }

        if theme_name:
            presentation["theme_name"] = theme_name

        # Add to metadata
        self.metadata["presentations"].append(presentation)
        self._save_metadata()

        return slug

    def update_presentation(
        self,
        identifier: str,
        gamma_id: Optional[str] = None,
        gamma_url: Optional[str] = None,
        num_cards: Optional[int] = None
    ):
        """
        Update an existing presentation's metadata.

        Args:
            identifier: Presentation ID, local file path, or Gamma URL
            gamma_id: New Gamma generation ID
            gamma_url: New Gamma URL
            num_cards: Updated number of cards

        Raises:
            ValueError: If presentation not found
        """
        presentation = self.find_presentation(identifier)
        if not presentation:
            raise ValueError(f"Presentation not found: {identifier}")

        # Update fields
        if gamma_id:
            presentation["gamma_id"] = gamma_id
        if gamma_url:
            presentation["gamma_url"] = gamma_url
        if num_cards:
            presentation["num_cards"] = num_cards

        # Update timestamp
        presentation["updated_at"] = datetime.utcnow().isoformat() + "Z"

        self._save_metadata()

    def find_presentation(self, identifier: str) -> Optional[Dict[str, Any]]:
        """
        Find a presentation by ID, local file path, or Gamma URL.

        Args:
            identifier: Presentation ID, local file path, or Gamma URL

        Returns:
            Presentation metadata dictionary, or None if not found
        """
        for presentation in self.metadata["presentations"]:
            if (
                presentation["id"] == identifier
                or presentation["local_file"] == identifier
                or presentation["gamma_url"] == identifier
                or identifier in presentation["gamma_url"]
            ):
                return presentation
        return None

    def list_presentations(self) -> List[Dict[str, Any]]:
        """
        Get all presentations.

        Returns:
            List of presentation metadata dictionaries
        """
        return self.metadata["presentations"]

    def delete_presentation(self, identifier: str):
        """
        Delete a presentation from metadata.

        Args:
            identifier: Presentation ID, local file path, or Gamma URL

        Raises:
            ValueError: If presentation not found
        """
        presentation = self.find_presentation(identifier)
        if not presentation:
            raise ValueError(f"Presentation not found: {identifier}")

        self.metadata["presentations"].remove(presentation)
        self._save_metadata()

    def _generate_slug(self, title: str) -> str:
        """
        Generate a URL-friendly slug from the title.

        Args:
            title: Presentation title

        Returns:
            URL-friendly slug
        """
        # Convert to lowercase and replace spaces with hyphens
        slug = title.lower().replace(" ", "-")

        # Remove special characters
        slug = "".join(c for c in slug if c.isalnum() or c == "-")

        # Ensure uniqueness
        base_slug = slug
        counter = 1
        while any(p["id"] == slug for p in self.metadata["presentations"]):
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about tracked presentations.

        Returns:
            Dictionary with presentation statistics
        """
        presentations = self.metadata["presentations"]

        return {
            "total_presentations": len(presentations),
            "formats": {
                "presentation": len([p for p in presentations if p.get("format") == "presentation"]),
                "document": len([p for p in presentations if p.get("format") == "document"]),
                "social": len([p for p in presentations if p.get("format") == "social"]),
            },
            "total_cards": sum(p.get("num_cards", 0) for p in presentations),
            "most_recent": presentations[-1] if presentations else None
        }


# Convenience functions for quick access
def add_presentation_quick(
    local_file: str,
    gamma_id: str,
    gamma_url: str,
    title: str,
    **kwargs
) -> str:
    """
    Quickly add a presentation to metadata.

    Args:
        local_file: Path to local markdown file
        gamma_id: Gamma generation ID
        gamma_url: Gamma presentation URL
        title: Presentation title
        **kwargs: Additional metadata fields

    Returns:
        Generated presentation ID
    """
    metadata = GammaMetadata()
    return metadata.add_presentation(
        local_file=local_file,
        gamma_id=gamma_id,
        gamma_url=gamma_url,
        title=title,
        **kwargs
    )


def find_presentation_quick(identifier: str) -> Optional[Dict[str, Any]]:
    """
    Quickly find a presentation by identifier.

    Args:
        identifier: Presentation ID, local file, or Gamma URL

    Returns:
        Presentation metadata, or None if not found
    """
    metadata = GammaMetadata()
    return metadata.find_presentation(identifier)
