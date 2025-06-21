"""Tests for JSON extraction functionality."""

from json_viewer.extractor import extract_json_from_text


def test_extract_json_object():
    """Test extracting JSON object from text."""
    text = 'Some text {"name": "John", "age": 30} more text'
    result = extract_json_from_text(text)
    assert result == '{"name": "John", "age": 30}'


def test_extract_json_array():
    """Test extracting JSON array from text."""
    text = "Some text [1, 2, 3] more text"
    result = extract_json_from_text(text)
    assert result == "[1, 2, 3]"


def test_extract_pure_json():
    """Test extracting pure JSON."""
    text = '{"name": "John", "age": 30}'
    result = extract_json_from_text(text)
    assert result == '{"name": "John", "age": 30}'


def test_extract_no_json():
    """Test text with no valid JSON."""
    text = "This is just regular text with no JSON"
    result = extract_json_from_text(text)
    assert result is None


def test_extract_malformed_json():
    """Test text with malformed JSON."""
    text = 'Some text {"name": "John", "age":} more text'
    result = extract_json_from_text(text)
    assert result is None


def test_extract_empty_text():
    """Test empty text."""
    text = ""
    result = extract_json_from_text(text)
    assert result is None


def test_extract_whitespace_only():
    """Test whitespace-only text."""
    text = "   \n\t  "
    result = extract_json_from_text(text)
    assert result is None


def test_extract_nested_json():
    """Test extracting nested JSON."""
    text = 'Data: {"user": {"name": "John", "details": {"age": 30}}} end'
    result = extract_json_from_text(text)
    assert result == '{"user": {"name": "John", "details": {"age": 30}}}'
