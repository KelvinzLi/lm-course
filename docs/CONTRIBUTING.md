# Contributing Guide

## Development Setup

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.zshrc  # or restart terminal

# Clone and setup
git clone https://github.com/yourusername/lm-course.git
cd lm-course
uv sync --group dev  # Installs dev tools (pytest, black, flake8)
```

## Adding Dependencies

```bash
# Automatically updates pyproject.toml
uv add package-name

# For development tools
uv add --group dev tool-name
```

## Code Style

### Function Naming & Organization
- **Public functions**: Add to `__init__.py` if used across multiple lectures
- **Private helpers**: Prefix with `_` and don't export
- **Package-level exports**: Only for the most commonly used functions

### Adding New Utilities

1. **Create function** in appropriate module (e.g., `lmcourse/utils/visualization.py`)
2. **Export in module** `__init__.py` if it's public API
3. **Add to package level** only if used in 3+ lectures

Example:
```python
# lmcourse/utils/new_module.py
def helpful_function():
    """Does something useful."""
    pass

# lmcourse/utils/__init__.py  
from .new_module import helpful_function

# lmcourse/__init__.py (only if widely used)
from .utils import helpful_function
```

## Import System

The course uses an installable package system:

```python
# Students can import from anywhere:
from lmcourse.utils import plot_attention_heatmap
from lmcourse.models import SomeModel

# Direct imports always work:
from lmcourse.utils.visualization import any_function
```

## Testing

```bash
uv run pytest                        # Run tests
uv run pytest --nbval lectures/     # Test all notebooks
```

## Code Quality

```bash
uv run black .                       # Format code
uv run flake8 lmcourse/             # Check style
```

## Coding Standards

Follow the user rules for:
- Procedural, C-like code style
- Type hints for all functions
- Short functions (<50 statements)
- Snake_case naming
- Docstrings for public functions

## Documentation

- **Lecture content**: Use `lectures/*/README.md`
- **Course overview**: Update main `README.md`
- **Setup changes**: Update `docs/SETUP.md`

Keep documentation minimal and focused!
