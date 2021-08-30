.PHONY: lint
lint:
	flake8
	mypy .

.PHONY: test
test:
	pytest

.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: format
format:
	isort .
	black .

.PHONY: main
main:
	python3 -m src.main
