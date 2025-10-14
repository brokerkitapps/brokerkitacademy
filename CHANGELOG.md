# Changelog

All notable changes to the Brokerkit Academy project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-13

### Added
- Complete Gamma API integration for presentation management
  - Python API client with full Generate API support
  - Metadata tracking system linking local files to Gamma URLs
  - Theme management with caching
  - CLI scripts for creating and viewing presentations
- `/create_slides` slash command for creating presentations from ideas or files
- `/update_slides` slash command for regenerating presentations with updated content
- Comprehensive documentation:
  - Gamma API Quick Start Guide
  - Complete API documentation
  - Example presentation template
- Python best practices implementation:
  - `pyproject.toml` for modern Python packaging
  - `LICENSE` file for proprietary software
  - `CONTRIBUTING.md` with development guidelines
  - Type hints throughout codebase
  - Comprehensive docstrings
- Project restructuring:
  - `assets/content/` for handouts and guides (formerly `docs/`)
  - `assets/slides/` for presentation content (formerly `slides/`)
  - `docs/` for project documentation
- Customer playbooks for Brokerboost services:
  - AI Outbound Recruiter Customer Playbook
  - Job Ads Customer Playbook
  - Social Ads Customer Playbook

### Changed
- Reorganized repository structure for better clarity
- Updated all file paths in code and documentation
- Moved temporary files to `tmp/` (now gitignored)

### Fixed
- Path resolution issues in metadata tracking
- File reference consistency across documentation

## [1.0.1] - 2025-10-13

### Added
- Comprehensive test suite with pytest fixtures
  - Unit tests for GammaClient with mocking
  - Unit tests for GammaMetadata tracking
  - Unit tests for ThemeManager
  - Shared fixtures in conftest.py
- `.env.example` template file for new developers
- `py.typed` marker file for PEP 561 type checking support
- `MANIFEST.in` for proper packaging of non-Python files
- `mypy` to requirements.txt for type checking consistency

### Changed
- Updated README.md with correct installation steps
- Updated README.md with accurate CLI command examples
- Synced requirements.txt with pyproject.toml dependencies

### Removed
- Deprecated `scripts/gamma/` directory (all code now in `src/`)
- Old scripts directory structure completely cleaned up

### Fixed
- Package now properly installed in editable mode
- CLI tools (`create-gamma-slides`, `view-gamma-metadata`) verified working
- Python imports verified functional
- Type checking configuration completed

## [Unreleased]

### Planned
- Pre-commit hooks for automated quality checks
- CI/CD pipeline for automated testing
- Additional slash commands for content types
- Integration tests for Gamma API
- Performance benchmarking tools

---

## Version History Legend

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security vulnerability fixes

## Links

- [Repository](https://github.com/brokerkitapps/brokerkitacademy)
- [Issues](https://github.com/brokerkitapps/brokerkitacademy/issues)
- [Gamma API Documentation](https://developers.gamma.app/)
