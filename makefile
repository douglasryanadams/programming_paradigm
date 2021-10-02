.PHONY: run clean test lint


test:
	poetry run pytest -s

lint:
	poetry run pylint ./app && poetry run mypy ./app

run:
	poetry run uvicorn app.main:app --reload