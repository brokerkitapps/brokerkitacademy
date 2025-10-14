#!/usr/bin/env python3
"""
View Gamma Metadata - Helper Script

This script displays all tracked Gamma presentations in a readable format.

Usage:
    python view_metadata.py
    python view_metadata.py --stats
    python view_metadata.py --search "agent recruiting"
"""

import sys
import argparse
from pathlib import Path
from typing import Optional

from brokerkitacademy.gamma.metadata import GammaMetadata


def format_presentation(pres: dict, index: int) -> str:
    """Format a presentation entry for display"""
    lines = [
        f"\n{'='*70}",
        f"#{index + 1} - {pres.get('title', 'Untitled')}",
        f"{'='*70}",
        f"  ID: {pres.get('id', 'N/A')}",
        f"  Local File: {pres.get('local_file', 'N/A')}",
        f"  Gamma URL: {pres.get('gamma_url', 'N/A')}",
        f"  Format: {pres.get('format', 'N/A')}",
        f"  Cards: {pres.get('num_cards', 'N/A')}",
    ]

    if pres.get('theme_name'):
        lines.append(f"  Theme: {pres['theme_name']}")

    lines.extend([
        f"  Created: {pres.get('created_at', 'N/A')}",
        f"  Updated: {pres.get('updated_at', 'N/A')}",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="View tracked Gamma presentations"
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics only"
    )

    parser.add_argument(
        "--search",
        type=str,
        help="Search for presentations by title or file"
    )

    args = parser.parse_args()

    # Initialize metadata
    metadata = GammaMetadata()

    # Show stats
    if args.stats:
        stats = metadata.get_stats()
        print("\n" + "="*70)
        print("GAMMA PRESENTATIONS STATISTICS")
        print("="*70)
        print(f"\nTotal Presentations: {stats['total_presentations']}")
        print(f"\nFormats:")
        print(f"  - Presentations: {stats['formats']['presentation']}")
        print(f"  - Documents: {stats['formats']['document']}")
        print(f"  - Social: {stats['formats']['social']}")
        print(f"\nTotal Cards: {stats['total_cards']}")

        if stats['most_recent']:
            print(f"\nMost Recent:")
            print(f"  {stats['most_recent']['title']}")
            print(f"  {stats['most_recent']['created_at']}")

        print("\n" + "="*70 + "\n")
        return 0

    # Get all presentations
    presentations = metadata.list_presentations()

    if not presentations:
        print("\n📭 No presentations tracked yet.")
        print("Create your first presentation with:")
        print("  /create_slides your topic here\n")
        return 0

    # Filter by search if provided
    if args.search:
        search_lower = args.search.lower()
        presentations = [
            p for p in presentations
            if (search_lower in p.get('title', '').lower() or
                search_lower in p.get('local_file', '').lower())
        ]

        if not presentations:
            print(f"\n🔍 No presentations found matching: {args.search}\n")
            return 0

    # Display presentations
    print("\n" + "="*70)
    print(f"TRACKED GAMMA PRESENTATIONS ({len(presentations)} total)")
    print("="*70)

    for i, pres in enumerate(presentations):
        print(format_presentation(pres, i))

    print("\n" + "="*70 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
