ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim

ENV PYTHONUNBUFFERED=1 \
  # pip
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry
  POETRY_VIRTUALENVS_CREATE=false

# slim specific
RUN apt-get update && apt install -y curl

# poetry install
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /code

# Project dependencies
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-ansi --no-interaction
