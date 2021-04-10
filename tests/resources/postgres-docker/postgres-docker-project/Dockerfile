from python:3.8-slim AS postgres_docker_project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

WORKDIR /app

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

COPY ./pyproject.toml ./poetry.lock* /app/
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false

RUN poetry install --no-root --no-dev \
    && rm pyproject.toml poetry.lock*

COPY ./postgres_docker_project postgres_docker_project

CMD ["sh", "./scripts/start.sh"]
