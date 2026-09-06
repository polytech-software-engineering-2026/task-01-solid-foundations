.PHONY: install hooks lint format test check check-volume

install:
	uv sync

hooks:
	uv run pre-commit install

lint:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy katas

format:
	uv run ruff check --fix .
	uv run ruff format .

test:
	uv run pytest tests -q

ref-tests:
	uv run pytest tests tests_reference -q

check: lint ref-tests

check-volume:
	uv run python scripts/check_volume.py
