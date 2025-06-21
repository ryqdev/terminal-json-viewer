import json
import sys
import argparse
from pathlib import Path
import pyperclip
import re


def extract_json_from_text(text):
    """Extract JSON data from text that may contain non-JSON content."""
    text = text.strip()
    
    # Try to find JSON-like patterns
    json_patterns = [
        r'\{.*\}',  # Object pattern
        r'\[.*\]',  # Array pattern
    ]
    
    for pattern in json_patterns:
        matches = re.findall(pattern, text, re.DOTALL)
        for match in matches:
            try:
                json.loads(match)
                return match
            except json.JSONDecodeError:
                continue
    
    # If no valid JSON found in patterns, try the whole text
    try:
        json.loads(text)
        return text
    except json.JSONDecodeError:
        pass
    
    return None


def format_json(data, indent=2):
    return json.dumps(data, indent=indent, ensure_ascii=False, sort_keys=True)


def main():
    parser = argparse.ArgumentParser(description="View and format JSON files")
    parser.add_argument("file", nargs="?", help="JSON file to view (stdin if not provided)")
    parser.add_argument("-i", "--indent", type=int, default=2, help="Indentation level (default: 2)")
    parser.add_argument("-c", "--compact", action="store_true", help="Compact output (no indentation)")
    parser.add_argument("-k", "--keys", action="store_true", help="Show only keys")
    parser.add_argument("-p", "--pasteboard", action="store_true", help="Read JSON data from clipboard")
    parser.add_argument("-e", "--extract", action="store_true", help="Extract JSON from text that contains non-JSON content")
    
    args = parser.parse_args()
    
    try:
        if args.pasteboard and args.file:
            print("Error: Cannot use both --pasteboard and file argument", file=sys.stderr)
            sys.exit(1)
        
        if args.pasteboard:
            try:
                content = pyperclip.paste()
            except Exception as e:
                print(f"Error: Failed to read from clipboard - {e}", file=sys.stderr)
                sys.exit(1)
        elif args.file:
            file_path = Path(args.file)
            if not file_path.exists():
                print(f"Error: File '{args.file}' not found", file=sys.stderr)
                sys.exit(1)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = sys.stdin.read()
        
        if not content.strip():
            print("Error: No JSON content provided", file=sys.stderr)
            sys.exit(1)
        
        # Extract JSON if requested or if direct parsing fails
        if args.extract:
            json_content = extract_json_from_text(content)
            if json_content is None:
                print("Error: No valid JSON found in the provided text", file=sys.stderr)
                sys.exit(1)
            content = json_content
        
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            # If direct parsing fails, try extracting JSON
            json_content = extract_json_from_text(content)
            if json_content is None:
                print(f"Error: Invalid JSON - {e}", file=sys.stderr)
                print("Tip: Use --extract flag to extract JSON from text containing non-JSON content", file=sys.stderr)
                sys.exit(1)
            data = json.loads(json_content)
        
        if args.keys:
            if isinstance(data, dict):
                for key in data.keys():
                    print(key)
            else:
                print("Error: --keys option only works with JSON objects", file=sys.stderr)
                sys.exit(1)
        elif args.compact:
            print(json.dumps(data, separators=(',', ':'), ensure_ascii=False))
        else:
            print(format_json(data, args.indent))
            
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
