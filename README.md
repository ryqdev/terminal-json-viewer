# terminal-json-viewer

A command-line tool for viewing and formatting JSON files with various output options.

## Installation

Install directly from GitHub using one of these methods:

**Using uv (recommended):**
```bash
uv tool install git+https://github.com/ryqdev/terminal-json-viewer.git
```

**Using pip:**
```bash
pip install git+https://github.com/ryqdev/terminal-json-viewer.git
```

**Using pipx:**
```bash
pipx install git+https://github.com/ryqdev/terminal-json-viewer.git
```

## Usage

After installation, use the `tjv` command:

```bash
# View a JSON file
tjv test.json

# Read from stdin
cat data.json | tjv

# Read from clipboard
tjv --pasteboard

# Compact output
tjv test.json --compact

# Show only keys
tjv test.json --keys

# Custom indentation
tjv test.json --indent 4

# Extract JSON from text containing non-JSON content
tjv mixed-content.txt --extract
```

## Options

- `-i, --indent`: Set indentation level (default: 2)
- `-c, --compact`: Compact output with no indentation
- `-k, --keys`: Show only the keys of JSON objects
- `-p, --pasteboard`: Read JSON data from clipboard
- `-e, --extract`: Extract JSON from text that contains non-JSON content
