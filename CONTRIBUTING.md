# Contributing to Brokerkit Academy

Thank you for contributing to Brokerkit Academy! This guide will help you understand our development process and standards.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git and GitHub CLI (`gh`)
- Gamma Pro/Ultra/Team/Business account
- Access to Brokerkit internal resources

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/brokerkitapps/brokerkitacademy.git
cd brokerkitacademy

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies (including dev dependencies)
pip install -r requirements.txt
pip install -e ".[dev]"  # If using pyproject.toml

# Configure API credentials
cp .env.example .env
# Edit .env and add your GAMMA_API_KEY
```

## Development Workflow

### Branching Strategy

- `main` - Production-ready code
- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation updates

### Making Changes

1. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clear, concise code
   - Follow PEP 8 style guidelines
   - Add docstrings to all functions and classes
   - Include type hints where appropriate

3. **Test your changes**:
   ```bash
   # Run tests
   pytest

   # Format code
   black .

   # Lint code
   flake8 .
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

## Code Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting (line length: 88)
- Use [Flake8](https://flake8.pycqa.org/) for linting
- Maximum line length: 88 characters

### Commit Message Format

Use conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(gamma): add theme selection support

Add ability to specify custom themes when creating presentations
via the Gamma API.

Closes #123
```

```
fix(metadata): correct file path resolution

Fix bug where metadata file path was incorrectly calculated on
Windows systems.
```

### Documentation

- Add docstrings to all public functions, classes, and modules
- Use Google-style docstrings
- Update README.md for significant changes
- Add inline comments for complex logic

**Docstring Example**:
```python
def create_presentation(
    input_text: str,
    num_cards: int = 15,
    theme_name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new Gamma presentation.

    Args:
        input_text: Content for the presentation (1-100,000 tokens)
        num_cards: Number of slides to generate (default: 15)
        theme_name: Optional theme name for visual styling

    Returns:
        Dictionary containing generation_id, status, and gamma_url

    Raises:
        GammaAPIError: If the API request fails
    """
```

### Type Hints

Add type hints to function signatures:

```python
from typing import Dict, List, Optional, Any

def process_slides(
    slides: List[Dict[str, str]],
    theme: Optional[str] = None
) -> Dict[str, Any]:
    """Process slide data."""
    pass
```

## Testing

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Use descriptive test names: `test_feature_does_something`
- Test both success and failure cases

**Test Example**:
```python
import pytest
from scripts.gamma.gamma_client import GammaClient, GammaAPIError

def test_create_presentation_success():
    """Test successful presentation creation."""
    client = GammaClient()
    result = client.create_presentation(
        input_text="# Test Presentation",
        num_cards=10
    )
    assert "gammaUrl" in result
    assert result["status"] == "completed"

def test_create_presentation_invalid_input():
    """Test presentation creation with invalid input."""
    client = GammaClient()
    with pytest.raises(GammaAPIError):
        client.create_presentation(input_text="", num_cards=0)
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_gamma_client.py

# Run with coverage
pytest --cov=scripts --cov-report=html
```

## Pull Request Process

1. **Update documentation**: Ensure README.md and relevant docs are updated

2. **Update changelog**: Add entry to CHANGELOG.md

3. **Create pull request**:
   ```bash
   git push origin feature/your-feature-name
   gh pr create --title "feat: your feature" --body "Description of changes"
   ```

4. **PR checklist**:
   - [ ] Code follows style guidelines
   - [ ] Tests pass locally
   - [ ] New tests added for new features
   - [ ] Documentation updated
   - [ ] CHANGELOG.md updated
   - [ ] No merge conflicts

5. **Code review**: Address reviewer feedback promptly

6. **Merge**: Once approved, squash and merge to main

## Content Creation Guidelines

### Handouts and Guides

- Store in `assets/content/` directory
- Use clear, action-oriented language
- Include real-world examples
- Provide step-by-step instructions
- Test all workflows before publishing

### Presentation Slides

- Store markdown source in `assets/slides/` directory
- Use `/create_slides` or `/update_slides` commands
- Follow presentation template structure
- Aim for 15-25 slides for standard presentations
- Include actionable takeaways

### Naming Conventions

- Files: `kebab-case.md` (e.g., `agent-recruiting-strategies.md`)
- Variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`

## Need Help?

- **Questions**: Ask in the #academy-dev Slack channel
- **Bug Reports**: Create a GitHub issue
- **Feature Requests**: Discuss in team meetings first

## License

By contributing to Brokerkit Academy, you agree that your contributions will be
licensed under the proprietary Brokerkit license.

---

Thank you for helping make Brokerkit Academy better!
