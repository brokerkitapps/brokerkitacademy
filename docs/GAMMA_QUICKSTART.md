# Gamma API Integration - Quick Start Guide

## What's Been Built

A complete Python-based system for creating and managing Gamma presentations via API:

### Components
- **Python API Client** - Full-featured Gamma API wrapper
- **Metadata Tracking** - JSON database linking local files to Gamma URLs
- **Theme Management** - Browse and use Gamma themes
- **CLI Scripts** - Command-line tools for presentation creation
- **Slash Commands** - Easy Claude Code integration

## Quick Start

### 1. Use Slash Commands (Easiest)

#### Create a new presentation:
```
/create_slides Agent recruiting strategies for Q1 2025
```

This will:
- Generate comprehensive markdown content
- Save it to `assets/slides/agent-recruiting-strategies-q1-2025.md`
- Create presentation in Gamma with AI-enhanced visuals
- Return the Gamma URL to view

#### Update an existing presentation:
```
/update_slides assets/slides/agent-recruiting-strategies-q1-2025.md - add social media section
```

This will:
- Read and update the local markdown file
- Regenerate the presentation in Gamma
- Track the new version in metadata
- Return the new Gamma URL

### 2. Use Python Scripts Directly

#### Create from a markdown file:
```bash
python3 scripts/gamma/create_slides.py \
  --file assets/slides/my-presentation.md \
  --title "My Presentation" \
  --num-cards 20 \
  --verbose
```

#### Create from inline text:
```bash
python3 scripts/gamma/create_slides.py \
  --text "# My Presentation\n## Slide 1\nContent here" \
  --title "Quick Deck" \
  --num-cards 10
```

#### List available themes:
```bash
python3 scripts/gamma/create_slides.py --list-themes
```

#### Use a specific theme:
```bash
python3 scripts/gamma/create_slides.py \
  --file assets/slides/my-presentation.md \
  --title "Styled Presentation" \
  --theme "Berlin" \
  --num-cards 15
```

### 3. View Tracked Presentations

```bash
# View all presentations
python3 scripts/gamma/view_metadata.py

# View statistics
python3 scripts/gamma/view_metadata.py --stats

# Search presentations
python3 scripts/gamma/view_metadata.py --search "recruiting"
```

## Workflow Examples

### Example 1: Create from Scratch

**User Request:**
```
/create_slides A webinar about using Relitix data for agent recruiting
```

**What Happens:**
1. Claude generates comprehensive content about Relitix
2. Content saved to `assets/slides/relitix-agent-recruiting-webinar.md`
3. Python script creates Gamma presentation
4. Metadata tracked in `assets/slides/gamma_metadata.json`
5. You get the Gamma URL: `https://gamma.app/docs/xxxxxxxxxx`

### Example 2: Use Existing Content

**User Request:**
```
/create_slides assets/slides/customer-bootcamp-session-1.md
```

**What Happens:**
1. Claude reads the existing markdown file
2. Python script sends content to Gamma API
3. Gamma creates presentation with AI enhancements
4. Metadata links file to Gamma URL
5. You get the URL to view the presentation

### Example 3: Update Presentation

**User Request:**
```
/update_slides assets/slides/agent-recruiting.md - update statistics to Q4 2025 data
```

**What Happens:**
1. Claude finds presentation in metadata
2. Reads current markdown file
3. Updates statistics as requested
4. Regenerates presentation in Gamma
5. Updates metadata with new URL
6. You get both old and new URLs

## File Structure

```
brokerkitacademy/
├── scripts/
│   └── gamma/
│       ├── __init__.py
│       ├── gamma_client.py          # API client
│       ├── gamma_metadata.py        # Metadata tracking
│       ├── gamma_themes.py          # Theme management
│       ├── create_slides.py         # CLI script
│       ├── view_metadata.py         # View metadata
│       ├── README.md                # Full documentation
│       └── themes_cache.json        # (auto-generated)
│
├── .claude/commands/
│   ├── create_slides.md             # /create_slides command
│   └── update_slides.md             # /update_slides command
│
├── assets/slides/
│   ├── gamma_metadata.json          # Metadata database
│   ├── example-presentation-template.md
│   └── [your slide markdown files]
│
├── .env                              # Contains GAMMA_API_KEY
└── GAMMA_QUICKSTART.md              # This file
```

## How It Works

### Creating Presentations

1. **Content Creation**
   - Write or generate markdown content
   - Use clear headings (`#`, `##`) for slide structure
   - Include bullet points, examples, and descriptions

2. **Gamma API**
   - Content sent to Gamma's Generate API
   - Gamma's AI creates professional layouts
   - AI adds relevant stock images automatically
   - Theme applied for visual consistency

3. **Metadata Tracking**
   - Local file linked to Gamma URL
   - Creation date, update date tracked
   - Parameters stored (cards, theme, format)
   - Easy lookup by file or URL

### Updating Presentations

**Important:** Gamma API doesn't support editing existing presentations yet, so "update" means:
1. Edit the local markdown file
2. Regenerate a new presentation in Gamma
3. Get a new URL for the updated version
4. Metadata tracks both versions

### Gamma AI Enhancements

When you create a presentation, Gamma automatically:
- Creates professional slide layouts
- Adds relevant stock images (AI-generated, Unsplash, or GIPHY)
- Applies theme colors and fonts
- Formats text with visual hierarchy
- Adds subtle animations
- Generates charts and diagrams

Your markdown content provides the structure and information. Gamma makes it beautiful.

## Tips for Great Presentations

1. **Structure Content Well**
   - Use `#` for title, `##` for main sections
   - Keep bullet points concise
   - Include examples and context

2. **Right-Size Card Count**
   - 10-15 cards: Short presentations
   - 15-25 cards: Standard presentations
   - 25-40 cards: Training sessions

3. **Use Themes Consistently**
   - "Berlin" and "Cape" work well for professional content
   - Use same theme for related presentations
   - List themes with `--list-themes`

4. **Let Gamma Handle Visuals**
   - AI-generated images match your content
   - Don't worry about design details
   - Focus on clear, compelling content

5. **Version Control**
   - Commit markdown files to Git
   - Track changes over time
   - Regenerate from any version

## Troubleshooting

### "No API key found"
- Check `.env` file has `GAMMA_API_KEY=sk-gamma-xxxxx`
- Verify you have Gamma Pro or higher account

### "Rate limit exceeded"
- Gamma allows 50 generations per hour
- Wait before retrying
- Space out batch operations

### "File not found"
- Use absolute paths or paths relative to project root
- Check file exists with `ls assets/slides/`

### Script won't run
- Ensure Python 3.8+ installed: `python3 --version`
- Install dependencies: `pip install -r requirements.txt`
- Make script executable: `chmod +x scripts/gamma/create_slides.py`

### Metadata issues
- Check `assets/slides/gamma_metadata.json` is valid JSON
- Regenerate if corrupted: Delete file and recreate presentations

## API Limits and Features

### Rate Limits
- **Pro Users**: 50 generations/hour
- **Ultra Users**: 50 generations/hour, up to 75 cards

### Supported Features
- **Formats**: presentation, document, social
- **Card Range**: 1-60 (Pro), 1-75 (Ultra)
- **Themes**: 60+ professional themes
- **Images**: AI-generated, Unsplash, GIPHY
- **Languages**: 60+ languages supported
- **Export**: PDF, PPTX formats

## Next Steps

1. **Try it out:**
   ```
   /create_slides Test presentation about Brokerkit features
   ```

2. **Create real content:**
   ```
   /create_slides Customer bootcamp session 1 - Platform introduction
   ```

3. **View your presentations:**
   ```bash
   python3 scripts/gamma/view_metadata.py
   ```

4. **Read full docs:**
   - See `scripts/gamma/README.md` for complete documentation
   - Check `assets/slides/example-presentation-template.md` for content examples

## Support

- **Gamma API Docs**: https://developers.gamma.app/
- **Get API Key**: https://gamma.app (Account Settings → API)
- **Brokerkit Team**: Contact internally for questions

---

**Ready to create amazing presentations? Start with `/create_slides` now!**
