test:
	poetry run black .
	poetry run flake8 .
	poetry run pytest
