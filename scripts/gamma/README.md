# Gamma API Integration

Python scripts and utilities for creating and managing Gamma presentations via the Gamma Generate API.

## Overview

This package provides a complete solution for working with Gamma presentations:
- Create presentations from markdown content
- Track metadata linking local files to Gamma URLs
- Support for all Gamma API features (themes, images, formats)
- Automatic status polling and error handling

## Components

### Core Modules

#### `gamma_client.py`
Python client for the Gamma Generate API with full support for:
- Creating presentations, documents, and social content
- Automatic status polling until completion
- All API parameters (themes, cards, images, formats)
- Comprehensive error handling

#### `gamma_metadata.py`
Metadata tracking system that maintains a JSON database linking:
- Local markdown files
- Gamma presentation IDs and URLs
- Creation and update timestamps
- Presentation parameters (title, format, card count, theme)

#### `gamma_themes.py`
Theme management utilities with:
- Fetch available themes from API
- Local caching to reduce API calls
- Default theme fallbacks
- Theme validation and search

### CLI Scripts

#### `create_slides.py`
Command-line script for creating Gamma presentations:

```bash
# Create from file
python3 scripts/gamma/create_slides.py \
  --file slides/my-presentation.md \
  --title "My Presentation" \
  --num-cards 20 \
  --verbose

# Create from inline text
python3 scripts/gamma/create_slides.py \
  --text "Create a presentation about agent recruiting" \
  --title "Quick Deck" \
  --num-cards 10

# List available themes
python3 scripts/gamma/create_slides.py --list-themes

# Use specific theme
python3 scripts/gamma/create_slides.py \
  --file slides/my-presentation.md \
  --title "Styled Presentation" \
  --theme "Berlin" \
  --num-cards 15 \
  --verbose
```

**Options:**
- `--file PATH` - Markdown file with content
- `--text TEXT` - Inline text content
- `--title TITLE` - Presentation title (required)
- `--num-cards N` - Number of slides (default: 15)
- `--theme NAME` - Theme name
- `--format TYPE` - Format: presentation/document/social
- `--image-source TYPE` - Images: aiGenerated/unsplash/giphy
- `--list-themes` - List available themes
- `--verbose` - Print detailed output

## Slash Commands

Two Claude Code slash commands are available for easy interaction:

### `/create_slides`
Create a new Gamma presentation from an idea or existing content.

```
/create_slides Agent recruiting strategies for Q1 2025
/create_slides slides/existing-content.md
```

The command will:
1. Generate content if you provide an idea
2. Or use existing markdown file if provided
3. Save content to `slides/` directory
4. Create presentation in Gamma via API
5. Track metadata in `slides/gamma_metadata.json`
6. Return the Gamma URL

### `/update_slides`
Update an existing presentation (regenerates with new content).

```
/update_slides slides/agent-recruiting-q1-2025.md - add social media section
/update_slides https://gamma.app/docs/xxxxxxxxxx - update statistics
```

The command will:
1. Find the presentation by file path or Gamma URL
2. Read and update the local markdown file
3. Regenerate the presentation in Gamma
4. Update metadata with new URL
5. Return both old and new URLs

**Note:** Due to API limitations, "updating" means regenerating a new presentation with updated content rather than editing the existing one.

## Metadata Tracking

All presentations are tracked in `slides/gamma_metadata.json`:

```json
{
  "presentations": [
    {
      "id": "agent-recruiting-q1-2025",
      "local_file": "slides/agent-recruiting-q1-2025.md",
      "gamma_id": "XXXXXXXXXXX",
      "gamma_url": "https://gamma.app/docs/yyyyyyyyyy",
      "created_at": "2025-10-13T10:30:00Z",
      "updated_at": "2025-10-13T10:30:00Z",
      "title": "Agent Recruiting Strategies Q1 2025",
      "format": "presentation",
      "num_cards": 20,
      "theme_name": "Berlin"
    }
  ]
}
```

This enables:
- Quick lookup from file path or Gamma URL
- Version history tracking
- Presentation statistics and analytics
- Easy management of multiple presentations

## Python API Usage

### Quick Example

```python
from scripts.gamma.gamma_client import create_quick_presentation

# Create a presentation and get the URL
url = create_quick_presentation(
    input_text="# My Presentation\n\n## Slide 1\nContent here...",
    num_cards=15
)
print(f"View presentation: {url}")
```

### Full Example

```python
from scripts.gamma.gamma_client import GammaClient
from scripts.gamma.gamma_metadata import GammaMetadata

# Initialize clients
client = GammaClient()
metadata = GammaMetadata()

# Create presentation
result = client.create_presentation(
    input_text="# Agent Recruiting\n\n## Key Strategies...",
    format="presentation",
    num_cards=20,
    theme_name="Berlin",
    image_source="aiGenerated",
    wait_for_completion=True
)

# Save metadata
metadata.add_presentation(
    local_file="slides/agent-recruiting.md",
    gamma_id=result["generationId"],
    gamma_url=result["gammaUrl"],
    title="Agent Recruiting Strategies",
    num_cards=20,
    theme_name="Berlin"
)

print(f"Created: {result['gammaUrl']}")
```

### Find Presentations

```python
from scripts.gamma.gamma_metadata import find_presentation_quick

# Find by file path
pres = find_presentation_quick("slides/agent-recruiting.md")

# Find by URL
pres = find_presentation_quick("https://gamma.app/docs/xxxxxxxxxx")

# Find by ID
pres = find_presentation_quick("agent-recruiting")

if pres:
    print(f"Title: {pres['title']}")
    print(f"URL: {pres['gamma_url']}")
    print(f"Created: {pres['created_at']}")
```

## Gamma API Features

### Supported Parameters

- **Format**: presentation, document, social
- **Card Count**: 1-60 (Pro), 1-75 (Ultra)
- **Text Mode**: generate, condense, preserve
- **Themes**: 60+ professional themes
- **Images**: AI-generated, Unsplash, GIPHY
- **Image Styles**: photorealistic, artistic, etc.
- **Export**: PDF, PPTX formats
- **Languages**: 60+ languages supported

### AI Capabilities

Gamma's AI automatically:
- Creates professional layouts
- Adds relevant stock images
- Applies theme-based styling
- Formats content hierarchically
- Generates visual elements

### Rate Limits

- **Pro Users**: 50 generations per hour
- **Ultra Users**: 50 generations per hour (up to 75 cards)

## Workflow Examples

### Creating from Scratch

1. Define your content in markdown
2. Save to `slides/my-presentation.md`
3. Run `/create_slides slides/my-presentation.md`
4. Get Gamma URL instantly
5. Edit further in Gamma web interface if needed

### Updating Existing

1. Edit your local markdown file
2. Run `/update_slides slides/my-presentation.md`
3. Get new Gamma URL with updated content
4. Metadata tracks both versions

### Version Control

Since all content is stored as markdown files:
- Commit files to Git for version history
- Track changes over time
- Collaborate using standard Git workflows
- Regenerate presentations from any version

## Requirements

- Python 3.8+
- Gamma Pro/Ultra/Team/Business account
- Valid Gamma API key in `.env` file

## Installation

Dependencies are managed in `requirements.txt`:
```
requests>=2.31.0
python-dotenv>=1.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

## Configuration

Set your Gamma API key in `.env`:
```
GAMMA_API_KEY=sk-gamma-xxxxxxxxxxxxxxxx
```

Get your API key from: https://gamma.app (Account Settings → API)

## Error Handling

All modules include comprehensive error handling:
- Network errors and timeouts
- API rate limiting
- Invalid parameters
- Missing credentials
- File not found errors

Errors are raised as `GammaAPIError` exceptions with descriptive messages.

## Best Practices

1. **Content First**: Focus on creating great markdown content. Let Gamma handle the visuals.

2. **Version Control**: Always commit your markdown files to Git before creating presentations.

3. **Metadata Tracking**: Use the metadata system to track all presentations. Don't lose track of URLs!

4. **Theme Consistency**: Use consistent themes across related presentations for brand cohesion.

5. **Card Count**: Match card count to content:
   - 10-15 cards: Short presentations
   - 15-25 cards: Standard presentations
   - 25-40 cards: Training sessions/bootcamps

6. **AI Images**: Use AI-generated images for most content. They're created specifically for your content.

7. **Iterate**: Create initial version quickly, then refine in Gamma's web interface.

## Troubleshooting

### API Key Issues
- Ensure `.env` file exists with `GAMMA_API_KEY`
- Verify you have a Pro or higher account
- Check that your API key is active

### Rate Limiting
- Wait before retrying if you hit the 50/hour limit
- Consider spacing out batch operations

### Generation Failures
- Check content length (1-100,000 tokens)
- Verify all parameters are valid
- Use `--verbose` flag for detailed error messages

### Metadata Issues
- Check `slides/gamma_metadata.json` exists
- Ensure file has proper JSON formatting
- Fix by deleting and regenerating if corrupted

## Support

For Gamma API documentation: https://developers.gamma.app/

For Brokerkit Academy questions: Contact the internal team

## License

Proprietary to Brokerkit. Internal use only.
