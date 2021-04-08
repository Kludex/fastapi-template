from python:3.9-slim AS {{ cookiecutter.package_name }}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

WORKDIR /app

{% if cookiecutter.packaging == 'poetry' -%}
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
{%- else %}
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt
{%- endif %}

COPY ./{{ cookiecutter.package_name }} {{ cookiecutter.package_name }}

{% if cookiecutter.run_server == 'CLI' -%}
CMD ["uvicorn", "{{cookiecutter.package_name}}.main:app", "--host", "0.0.0.0"]
{% else -%}
CMD ["python", "-m", "{{cookiecutter.package_name}}"]
{% endif -%}
