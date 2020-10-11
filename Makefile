install:
	pip install -r requirements.txt

lint:
	flake8
	black --check --diff .
	isort --check --diff .
	python -m mypy --config-file setup.cfg --pretty .

test:
	pytest tests -vv

.PHONY: install lint test
