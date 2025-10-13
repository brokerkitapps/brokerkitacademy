# Brokerkit Academy Content Creation Project

## Project Overview

This repository is dedicated to creating training content for **Brokerkit Academy**, where we educate residential real estate brokerages and team leaders in the U.S. and Canada on agent recruiting, onboarding, and retention strategies using the Brokerkit platform.

## About Brokerkit Academy

### Mission
Brokerkit Academy provides comprehensive training programs that combine:
- **Technology Platform Training**: How to effectively use Brokerkit's tech platform and data tools
- **Recruiting Best Practices**: Proven strategies for residential real estate agent recruiting
- **Retention Strategies**: Techniques for onboarding and retaining top real estate agents
- **Data-Driven Insights**: Leveraging MLS data through integrations like Relitix

### Training Offerings

#### 1. Brokerkit Customer Bootcamp
Comprehensive training program covering:
- Platform fundamentals and navigation
- Advanced recruiting workflows
- Data analysis and reporting
- Integration utilization (Relitix and others)

#### 2. Webinars
Regular online sessions focusing on:
- Specific recruiting tactics
- Seasonal strategies
- Platform feature deep-dives
- Q&A with industry experts

#### 3. Training Materials
- Call scripts for agent outreach
- Handouts and quick reference guides
- Presentation slides and decks
- Best practice documentation

## The Brokerkit Ecosystem

### Brokerkit Platform
The core technology platform providing:
- Agent recruiting pipeline management
- MLS data integration and analytics
- Automated workflows and reminders
- Performance tracking and reporting

### Relitix Integration
MLS data integration that enables:
- Real-time agent performance tracking
- Market intelligence and insights
- Competitive analysis tools
- Data-driven recruiting targeting

### Brokerboost
Our recruiting lead generation offering featuring:
- Job posting campaigns
- Social media advertising
- AI-driven LinkedIn outreach
- Automated email campaigns
- Multi-channel recruiting marketing

## Content Types

This repository supports creation of:

1. **Handouts and Guides** (stored in `docs/`)
   - Call scripts for recruiter-agent conversations
   - Quick reference cards
   - Checklists and workflows
   - Best practice guides

2. **Presentation Slides** (stored in `slides/`)
   - Bootcamp presentations
   - Webinar decks
   - Training modules
   - Feature announcements

3. **Scripts and Automation** (stored in `scripts/`)
   - Python scripts for content generation
   - Gamma API integration tools
   - Content templating utilities

## Technical Stack

### Python as the Preferred Language
All scripting and automation in this project uses **Python**. This includes:
- Gamma API integration scripts
- Content generation utilities
- Data processing and formatting
- Automation workflows

### Gamma Integration

#### About Gamma
Gamma.ai is an AI-powered presentation creation platform that enables:
- Rapid slide deck generation
- Professional design templates
- AI-assisted content creation
- Multi-format export options

#### API Access
- **Requirements**: Gamma Pro/Ultra/Team/Business account
- **API Key Format**: `sk-gamma-xxxxxxxx`
- **Rate Limits**: 50 presentations per day (Pro tier)
- **Documentation**: https://help.gamma.app/

#### MCP Server
Gamma has Model Context Protocol (MCP) server implementations available:
- Multiple GitHub implementations (nickloveinvesting/gamma-mcpserver, CryptoJym)
- Direct integration with Claude Code
- Presentation generation capabilities
- Document and social content creation

## Repository Structure

```
brokerkitacademy/
├── .claude/
│   └── commands/          # Custom Claude slash commands
├── docs/                  # Markdown handouts and guides
├── scripts/               # Python automation scripts
├── slides/                # Gamma slide deck content
├── tmp/                   # Temporary working files
├── .env                   # API credentials (not committed)
├── .gitignore            # Git ignore patterns
├── claude.md             # This file - project documentation
├── README.md             # Quick start guide
└── requirements.txt      # Python dependencies
```

## GitHub Repository

- **Organization**: brokerkitapps
- **Repository**: brokerkitacademy
- **URL**: https://github.com/brokerkitapps/brokerkitacademy

### Pushing to GitHub

This repository is managed using the GitHub CLI (`gh`). To push changes:

```bash
# First time setup
gh repo create brokerkitapps/brokerkitacademy --public --source=. --remote=origin --push

# Subsequent pushes
git add .
git commit -m "Your commit message"
git push origin main
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- GitHub CLI (`gh`) installed and authenticated
- Gamma Pro/Ultra/Team/Business account (for API access)

### Initial Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/brokerkitapps/brokerkitacademy.git
   cd brokerkitacademy
   ```

2. **Create Python virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API credentials**:
   - Copy `.env` file and add your Gamma API key
   - Get your API key from https://gamma.app (Account Settings → API)

5. **Start creating content**:
   - Use Claude slash commands in `.claude/commands/`
   - Run Python scripts in `scripts/`
   - Store handouts in `docs/`
   - Store presentations in `slides/`

## Development Workflow

### Creating Handouts
1. Draft content in markdown format
2. Store in `docs/` directory
3. Import into Google Docs for final formatting
4. Share with Academy participants

### Creating Slide Decks
1. Use Claude slash command `/create_academy_content`
2. Generate content using Gamma API via Python scripts
3. Review and refine in Gamma web interface
4. Export and store in `slides/` directory

### Version Control
- Commit markdown files and scripts to Git
- Use descriptive commit messages
- Tag releases for major content updates
- Push regularly to GitHub

## Best Practices

### Content Creation
- Focus on actionable, practical advice
- Use real-world examples from real estate recruiting
- Include specific Brokerkit platform references
- Provide step-by-step instructions with screenshots
- Test all scripts and call flows before publishing

### Code Quality
- Follow PEP 8 style guide for Python code
- Include docstrings for all functions
- Add error handling and logging
- Write modular, reusable code
- Comment complex logic

### Documentation
- Keep this `claude.md` file updated
- Document all API integrations
- Include setup instructions for new tools
- Maintain changelog for major updates

## Future Enhancements

- [ ] Automated content generation pipelines
- [ ] Integration with Brokerkit platform APIs
- [ ] Content analytics and engagement tracking
- [ ] Multi-language support for Canadian markets
- [ ] AI-powered content personalization
- [ ] Automated slide deck generation from markdown
- [ ] Integration with learning management systems

## Support and Contact

For questions or contributions to Brokerkit Academy content:
- **Internal Team**: Contact the Academy content team
- **GitHub Issues**: Report bugs or suggest features
- **Pull Requests**: Submit content improvements

## License

This repository is proprietary to Brokerkit and intended for internal use only.

---

*Last Updated: October 2025*
