app:
	@poetry run python app.py

test:
	@poetry run black .
	@poetry run flake8 .
	@poetry run pytest

docker_build:
	@docker build -t test_task -f Dockerfile .

docker_build_dev:
	@docker build -t test_task_dev -f dev.Dockerfile .

docker_app:
	@make docker_build && \
		docker run --rm -it -v ${PWD}:/code test_task \
		/bin/bash -c "poetry run python app.py"

docker_test:
	@make docker_build_dev && \
		docker run --rm -it -v ${PWD}:/code test_task_dev \
		/bin/bash -c "poetry run black . && poetry run flake8 . && poetry run pytest"
