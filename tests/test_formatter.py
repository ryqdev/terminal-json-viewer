"""Tests for JSON formatting functionality."""

from json_viewer.formatter import format_compact, format_json


def test_format_json_basic():
    """Test basic JSON formatting."""
    data = {"name": "John", "age": 30}
    result = format_json(data, indent=2)
    expected = '{\n  "age": 30,\n  "name": "John"\n}'
    assert result == expected


def test_format_json_custom_indent():
    """Test JSON formatting with custom indentation."""
    data = {"a": 1, "b": 2}
    result = format_json(data, indent=4)
    expected = '{\n    "a": 1,\n    "b": 2\n}'
    assert result == expected


def test_format_compact():
    """Test compact JSON formatting."""
    data = {"name": "John", "age": 30}
    result = format_compact(data)
    expected = '{"name":"John","age":30}'
    assert result == expected


def test_format_json_with_unicode():
    """Test JSON formatting with Unicode characters."""
    data = {"name": "José", "city": "São Paulo"}
    result = format_json(data)
    assert "José" in result
    assert "São Paulo" in result


def test_format_json_with_list():
    """Test JSON formatting with lists."""
    data = {"items": [1, 2, 3]}
    result = format_json(data)
    assert '"items": [\n    1,\n    2,\n    3\n  ]' in result
