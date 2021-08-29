.PHONY: lint
lint:
	flake8
	myypy

.PHONY: install
install:
	pip3 install -r requirements.txt

.PHONY: format
format:
	isort .
	black .
