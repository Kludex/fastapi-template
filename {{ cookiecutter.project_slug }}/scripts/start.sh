#! /usr/bin/env bash

{%- if cookiecutter.database == "PostgreSQL" %}
python scripts/wait_database.py
{%- endif %}

{% if cookiecutter.run_server == 'CLI' -%}
uvicorn "{{cookiecutter.package_name}}.main:app" --host "0.0.0.0" --port 8000
{% else -%}
python -m {{cookiecutter.package_name}}
{% endif -%}
