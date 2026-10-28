.PHONY: install dev test lint run demo clean

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check src tests

run:
	python -m msi_engine run --query "Onboard new employee Jane Doe" --workdir out

demo: install
	python -m msi_engine run --query "Onboard new employee Jane Doe" --workdir out

clean:
	rm -rf out .pytest_cache .ruff_cache **/__pycache__
