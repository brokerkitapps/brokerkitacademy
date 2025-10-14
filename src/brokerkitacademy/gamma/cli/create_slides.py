#!/usr/bin/env python3
"""
Create Gamma Slides - CLI Script

This script creates Gamma presentations from markdown content.
It handles API interaction, metadata tracking, and returns the Gamma URL.

Usage:
    python create_slides.py --file assets/slides/my-presentation.md --title "My Presentation"
    python create_slides.py --text "Create a presentation about..." --title "Quick Deck"
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from brokerkitacademy.gamma.client import GammaClient, GammaAPIError
from brokerkitacademy.gamma.metadata import GammaMetadata
from brokerkitacademy.gamma.themes import ThemeManager


def read_file_content(file_path: str) -> str:
    """
    Read content from a markdown file.

    Args:
        file_path: Path to the markdown file

    Returns:
        File contents as string

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def create_presentation(
    content: str,
    title: str,
    local_file: Optional[str] = None,
    num_cards: int = 15,
    theme_name: Optional[str] = None,
    format: str = "presentation",
    image_source: str = "unsplash",
    verbose: bool = False,
) -> dict:
    """
    Create a Gamma presentation and track metadata.

    Args:
        content: Markdown content for the presentation
        title: Presentation title
        local_file: Path to local markdown file (for metadata tracking)
        num_cards: Number of slides to generate
        theme_name: Theme to use for visual styling
        format: Format type (presentation/document/social)
        image_source: Image source - unsplash (default, professional stock photos),
                      aiGenerated, or giphy
        verbose: Print verbose output

    Returns:
        Dictionary with presentation details including gamma_url

    Raises:
        GammaAPIError: If API request fails
    """
    if verbose:
        print("🚀 Creating Gamma presentation...")
        print(f"   Title: {title}")
        print(f"   Cards: {num_cards}")
        if theme_name:
            print(f"   Theme: {theme_name}")
        print(f"   Format: {format}")
        image_desc = {
            "unsplash": "Professional stock photos from Unsplash",
            "aiGenerated": "AI-generated images",
            "giphy": "Animated GIFs from Giphy"
        }.get(image_source, image_source)
        print(f"   Images: {image_desc}")
        print()

    # Initialize clients
    client = GammaClient()
    metadata = GammaMetadata()

    # Create the presentation
    if verbose:
        print("📤 Sending request to Gamma API...")

    result = client.create_presentation(
        input_text=content,
        format=format,
        num_cards=num_cards,
        theme_name=theme_name,
        image_source=image_source,
        wait_for_completion=True,
    )

    gamma_id = result.get("generationId")
    gamma_url = result.get("gammaUrl")

    if not gamma_url:
        raise GammaAPIError("No gamma URL returned from API")

    if verbose:
        print("✅ Presentation created successfully!")
        print()

    # Track in metadata if local file is provided
    if local_file:
        presentation_id = metadata.add_presentation(
            local_file=local_file,
            gamma_id=gamma_id,
            gamma_url=gamma_url,
            title=title,
            format=format,
            num_cards=num_cards,
            theme_name=theme_name,
        )

        if verbose:
            print(f"📝 Metadata saved (ID: {presentation_id})")
            print()

    # Return results
    return {
        "gamma_id": gamma_id,
        "gamma_url": gamma_url,
        "title": title,
        "num_cards": num_cards,
        "local_file": local_file,
    }


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Create Gamma presentations from markdown content"
    )

    # Input source (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--file", type=str, help="Path to markdown file with presentation content"
    )
    input_group.add_argument(
        "--text", type=str, help="Inline text content for presentation"
    )

    # Required arguments
    parser.add_argument(
        "--title", type=str, required=True, help="Title for the presentation"
    )

    # Optional arguments
    parser.add_argument(
        "--num-cards",
        type=int,
        default=15,
        help="Number of slides to generate (default: 15)",
    )
    parser.add_argument("--theme", type=str, help="Theme name for visual styling")
    parser.add_argument(
        "--format",
        type=str,
        choices=["presentation", "document", "social"],
        default="presentation",
        help="Format type (default: presentation)",
    )
    parser.add_argument(
        "--image-source",
        type=str,
        choices=["aiGenerated", "unsplash", "giphy"],
        default="unsplash",
        help="Image source (default: unsplash for professional stock photos)",
    )
    parser.add_argument(
        "--list-themes", action="store_true", help="List available themes and exit"
    )
    parser.add_argument("--verbose", action="store_true", help="Print verbose output")

    args = parser.parse_args()

    # Handle --list-themes
    if args.list_themes:
        theme_manager = ThemeManager()
        theme_manager.print_themes()
        return 0

    try:
        # Get content from file or inline text
        if args.file:
            content = read_file_content(args.file)
            local_file = args.file
        else:
            content = args.text
            local_file = None

        # Create the presentation
        result = create_presentation(
            content=content,
            title=args.title,
            local_file=local_file,
            num_cards=args.num_cards,
            theme_name=args.theme,
            format=args.format,
            image_source=args.image_source,
            verbose=args.verbose,
        )

        # Output the URL
        print("=" * 60)
        print(f"🎉 Presentation Created Successfully!")
        print("=" * 60)
        print(f"\n📊 Title: {result['title']}")
        print(f"🎴 Cards: {result['num_cards']}")
        if local_file:
            print(f"📄 Local File: {result['local_file']}")
        print(f"\n🔗 View your presentation:")
        print(f"   {result['gamma_url']}")
        print()

        return 0

    except FileNotFoundError as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1

    except GammaAPIError as e:
        print(f"❌ Gamma API Error: {e}", file=sys.stderr)
        return 1

    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
