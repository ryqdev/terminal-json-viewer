# Terminal JSON Viewer

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

A professional command-line tool for viewing and formatting JSON files with various output options. Perfect for developers who work with JSON data in terminal environments.

## Features

- 🚀 **Fast and lightweight** - Built with performance in mind
- 📋 **Multiple input sources** - Files, stdin, or clipboard
- 🎨 **Flexible formatting** - Pretty-print, compact, or keys-only output
- 🔍 **Smart extraction** - Extract JSON from mixed content
- 🛠️ **Developer-friendly** - Intuitive CLI with helpful error messages
- 🔧 **Highly configurable** - Customize indentation and output format

## Installation

### Using uv (recommended)
```bash
uv tool install git+https://github.com/ryqdev/terminal-json-viewer.git
```

### Using pip
```bash
pip install git+https://github.com/ryqdev/terminal-json-viewer.git
```

### Using pipx
```bash
pipx install git+https://github.com/ryqdev/terminal-json-viewer.git
```

## Usage

After installation, use the `tjv` command:

### Basic Usage
```bash
# View a JSON file with pretty formatting
tjv data.json

# Read from stdin
cat data.json | tjv
echo '{"name": "John", "age": 30}' | tjv

# Read from clipboard (macOS/Linux/Windows)
tjv --pasteboard
```

### Formatting Options
```bash
# Compact output (no indentation)
tjv data.json --compact

# Custom indentation (default: 2 spaces)
tjv data.json --indent 4

# Show only object keys
tjv data.json --keys
```

### Advanced Features
```bash
# Extract JSON from mixed content
tjv log-file.txt --extract

# Combine options
tjv --pasteboard --compact
```

## CLI Options

| Option | Short | Description |
|--------|-------|-------------|
| `--indent N` | `-i N` | Set indentation level (default: 2) |
| `--compact` | `-c` | Compact output with no indentation |
| `--keys` | `-k` | Show only the keys of JSON objects |
| `--pasteboard` | `-p` | Read JSON data from clipboard |
| `--extract` | `-e` | Extract JSON from text containing non-JSON content |

## Examples

### Pretty-print a JSON file
```bash
$ tjv example.json
{
  "name": "John Doe",
  "age": 30,
  "skills": [
    "Python",
    "JavaScript",
    "Go"
  ]
}
```

### Extract JSON from log files
```bash
$ tjv server.log --extract
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "message": "Database connection failed"
}
```

### View only object keys
```bash
$ tjv data.json --keys
name
age
skills
address
```

## Development

### Setup
```bash
# Clone the repository
git clone https://github.com/ryqdev/terminal-json-viewer.git
cd terminal-json-viewer

# Install with development dependencies
make install-dev
```

### Testing
```bash
# Run tests
make test

# Run tests with coverage
make test-cov

# Run all checks (lint, type-check, test)
make check
```

### Code Quality
```bash
# Format code
make format

# Run linting
make lint

# Run type checking
make type-check
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python 3.12+
- Uses `pyperclip` for clipboard functionality
- Follows modern Python packaging standards
