"""Command-line interface for Terminal JSON Viewer."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

try:
    import pyperclip

    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

from .extractor import extract_json_from_text
from .formatter import format_compact, format_json


def get_input_content(args: argparse.Namespace) -> str:
    """Get input content from various sources."""
    if args.pasteboard:
        if not CLIPBOARD_AVAILABLE:
            print(
                "Error: pyperclip not available for clipboard access", file=sys.stderr
            )
            sys.exit(1)
        try:
            return pyperclip.paste()
        except Exception as e:
            print(f"Error: Failed to read from clipboard - {e}", file=sys.stderr)
            sys.exit(1)
    elif args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
        with open(file_path, encoding="utf-8") as f:
            return f.read()
    else:
        return sys.stdin.read()


def parse_json_content(content: str, extract: bool = False) -> Dict[str, Any]:
    """Parse JSON content with optional extraction."""
    if not content.strip():
        print("Error: No JSON content provided", file=sys.stderr)
        sys.exit(1)

    if extract:
        json_content = extract_json_from_text(content)
        if json_content is None:
            print("Error: No valid JSON found in the provided text", file=sys.stderr)
            sys.exit(1)
        content = json_content

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        json_content = extract_json_from_text(content)
        if json_content is None:
            print(f"Error: Invalid JSON - {e}", file=sys.stderr)
            print(
                "Tip: Use --extract flag to extract JSON from text containing non-JSON content",
                file=sys.stderr,
            )
            sys.exit(1)
        return json.loads(json_content)


def output_result(data: Dict[str, Any], args: argparse.Namespace) -> None:
    """Output the formatted result."""
    if args.keys:
        if isinstance(data, dict):
            for key in data.keys():
                print(key)
        else:
            print("Error: --keys option only works with JSON objects", file=sys.stderr)
            sys.exit(1)
    elif args.compact:
        print(format_compact(data))
    else:
        print(format_json(data, args.indent))


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        description="View and format JSON files", prog="tjv"
    )
    parser.add_argument(
        "file", nargs="?", help="JSON file to view (stdin if not provided)"
    )
    parser.add_argument(
        "-i", "--indent", type=int, default=2, help="Indentation level (default: 2)"
    )
    parser.add_argument(
        "-c", "--compact", action="store_true", help="Compact output (no indentation)"
    )
    parser.add_argument("-k", "--keys", action="store_true", help="Show only keys")
    parser.add_argument(
        "-p", "--pasteboard", action="store_true", help="Read JSON data from clipboard"
    )
    parser.add_argument(
        "-e",
        "--extract",
        action="store_true",
        help="Extract JSON from text that contains non-JSON content",
    )
    return parser


def main() -> None:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()

    try:
        if args.pasteboard and args.file:
            print(
                "Error: Cannot use both --pasteboard and file argument", file=sys.stderr
            )
            sys.exit(1)

        content = get_input_content(args)
        data = parse_json_content(content, args.extract)
        output_result(data, args)

    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
