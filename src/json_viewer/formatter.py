"""JSON formatting utilities."""

import json
from typing import Any


def format_json(data: Any, indent: int = 2) -> str:
    """Format JSON data with proper indentation and sorting.

    Args:
        data: JSON data to format
        indent: Number of spaces for indentation

    Returns:
        Formatted JSON string
    """
    return json.dumps(data, indent=indent, ensure_ascii=False, sort_keys=True)


def format_compact(data: Any) -> str:
    """Format JSON data in compact form.

    Args:
        data: JSON data to format

    Returns:
        Compact JSON string
    """
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False)
