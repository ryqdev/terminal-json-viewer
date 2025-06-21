"""JSON extraction utilities."""

import json
import re


def extract_json_from_text(text: str) -> str | None:
    """Extract JSON data from text that may contain non-JSON content.

    Args:
        text: Input text that may contain JSON data

    Returns:
        Valid JSON string if found, None otherwise
    """
    text = text.strip()

    if not text:
        return None

    json_patterns = [
        r"\{.*\}",  # Object pattern
        r"\[.*\]",  # Array pattern
    ]

    for pattern in json_patterns:
        matches = re.findall(pattern, text, re.DOTALL)
        for match in matches:
            try:
                json.loads(match)
                return match
            except json.JSONDecodeError:
                continue

    try:
        json.loads(text)
        return text
    except json.JSONDecodeError:
        pass

    return None
