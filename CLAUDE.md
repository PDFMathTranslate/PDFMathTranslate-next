# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment Setup

This project uses **uv** for Python package management, not Poetry. The project requires Python 3.10-3.13.

### Virtual Environment Setup
```bash
uv venv
source .venv/bin/activate  # Linux/Mac
uv sync --group dev  # Install dependencies including dev group
```

### Alternative Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -e .
pip install -e .[dev]  # Install with development dependencies
```

## Development Commands

### Testing
```bash
pytest  # Run all tests
pytest test/test_cache.py  # Run specific test file
pytest tests/config/  # Run tests in specific directory
```

### Code Quality
```bash
ruff check  # Lint code
ruff format  # Format code
ruff check --fix  # Auto-fix linting issues
```

### Building
```bash
python -m build  # Build distribution packages
```

### Version Management
```bash
bumpver update --patch  # Bump patch version
bumpver update --minor  # Bump minor version
```

## Project Architecture

### Core Components

**Main Entry Points:**
- `pdf2zh_next/main.py` - CLI interface and main entry point
- `pdf2zh_next/gui.py` - Gradio-based web UI
- `pdf2zh_next/http_api.py` - FastAPI HTTP server

**Translation Engine:**
- `pdf2zh_next/high_level.py` - High-level translation orchestration using BabelDOC backend
- `pdf2zh_next/translator/` - Translation service implementations and rate limiting
- `pdf2zh_next/translator/translator_impl/` - Individual translator implementations (OpenAI, Azure, Google, SiliconFlow, etc.)

**Configuration System:**
- `pdf2zh_next/config/` - Pydantic-based configuration management
- `pdf2zh_next/config/model.py` - Core settings models with validation
- `pdf2zh_next/config/main.py` - Configuration manager with environment variable support

### Translation Architecture

The project uses a two-layer architecture:
1. **BabelDOC Backend** - Handles PDF parsing, layout analysis, and document reconstruction
2. **PDF2ZH Translation Layer** - Manages translation services, rate limiting, and caching

Translation services are implemented as plugins in `translator_impl/` following the `BaseTranslator` interface with built-in rate limiting via `BaseRateLimiter`.

### Configuration Model

Settings are defined using Pydantic models with environment variable support:
- Basic settings (debug, GUI mode, input files)
- GUI settings (server port, authentication, sharing)  
- Translation settings (language codes, output modes, rate limits)
- Service-specific settings (API keys, endpoints, model parameters)

## Testing Strategy

- Unit tests use `unittest` framework
- Test files located in both `test/` and `tests/` directories  
- Cache functionality tested with in-memory test database
- Configuration testing with Pydantic model validation

## Key Dependencies

- **BabelDOC** - Core PDF processing backend
- **Gradio** - Web UI framework (version <5.36 due to compatibility)
- **FastAPI/Uvicorn** - HTTP API server
- **PyMuPDF** - PDF manipulation (version <1.25.3 for ARM64 compatibility)
- **Pydantic** - Configuration validation and settings management
- **Rich** - Terminal output formatting and logging

## Translation Services

Supported services include OpenAI, Azure OpenAI, Google Translate, DeepL, SiliconFlow, Ollama, Xinference, and others. Each service implements rate limiting and async translation capabilities.

## Scripts and Entry Points

- `pdf2zh`, `pdf2zh2`, `pdf2zh_next` - CLI commands (all point to same entry)
- `script/setup.bat` - Windows installer script
- Docker support with multiple Dockerfile variants in `script/`