.PHONY: install install-dev test lint format type-check clean build help

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	uv sync

install-dev: ## Install development dependencies
	uv sync --extra dev

test: ## Run tests
	uv run pytest -v

test-cov: ## Run tests with coverage
	uv run pytest --cov=json_viewer --cov-report=term-missing --cov-report=html

lint: ## Run linting checks
	uv run ruff check .
	uv run ruff format --check .

format: ## Format code
	uv run ruff format .
	uv run ruff check --fix .

type-check: ## Run type checking
	uv run mypy src/json_viewer

check: lint type-check test ## Run all checks (lint, type-check, test)

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Build the package
	uv build

publish: build ## Publish to PyPI
	uv publish

dev-install: ## Install in development mode
	uv pip install -e .