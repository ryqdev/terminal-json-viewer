"""Terminal JSON Viewer - A command-line tool for viewing and formatting JSON files."""

from .cli import main
from .extractor import extract_json_from_text
from .formatter import format_json

__version__ = "0.1.0"
__all__ = ["main", "format_json", "extract_json_from_text"]
