# Brokerkit Academy Content Creation

> Training content repository for Brokerkit Academy - empowering real estate brokerages and team leaders with recruiting and retention best practices.

## Quick Start

### Setup

```bash
# Clone the repository
git clone https://github.com/brokerkitapps/brokerkitacademy.git
cd brokerkitacademy

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies and package
pip install -r requirements.txt
pip install -e .

# Configure API credentials
# Copy .env.example to .env and add your Gamma API key
cp .env.example .env
# Edit .env file and add your GAMMA_API_KEY
```

### Create Your First Content

```bash
# Use Claude Code with custom slash commands
/create_slides agent recruiting call script

# Or use the installed CLI tools directly
create-gamma-slides --text "Agent Onboarding Best Practices" --title "Agent Onboarding" --num-cards 15

# Or use Python imports
python -c "from brokerkitacademy.gamma import create_quick_presentation; print(create_quick_presentation('# My Presentation', 15))"
```

## What's Inside

- **`assets/content/`** - Training handouts, call scripts, and guides (markdown format)
- **`assets/slides/`** - Presentation decks for bootcamps and webinars
- **`scripts/`** - Python automation for content generation
- **`.claude/commands/`** - Custom Claude Code commands

## About Brokerkit Academy

Brokerkit Academy trains residential real estate brokerages and team leaders on:
- Agent recruiting strategies
- Onboarding and retention tactics
- Effective use of the Brokerkit platform
- Leveraging MLS data through Relitix integration
- Maximizing ROI with Brokerboost lead generation

## Technologies

- **Python** - All scripting and automation
- **Gamma.ai** - AI-powered presentation creation
- **Markdown** - Documentation and handout format
- **GitHub** - Version control and collaboration

## Documentation

See [`claude.md`](./claude.md) for comprehensive project documentation including:
- Detailed project overview
- Brokerkit ecosystem explanation
- API integration guides
- Development workflows
- Best practices

## Contributing

This is an internal Brokerkit project. Team members should:
1. Create feature branches for new content
2. Follow Python PEP 8 style guidelines
3. Update documentation for new tools or workflows
4. Submit pull requests for review

## Support

- **Questions**: Contact the Academy content team
- **Issues**: Use GitHub Issues for bug reports
- **Ideas**: Submit feature requests via pull requests

---

**Repository**: https://github.com/brokerkitapps/brokerkitacademy
**Organization**: Brokerkit Apps
**Last Updated**: October 2025
