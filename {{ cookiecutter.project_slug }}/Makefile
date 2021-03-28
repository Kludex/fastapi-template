.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint:  ## Linter the code.
	isort {{ cookiecutter.package_name }} tests --check
	flake8 {{ cookiecutter.package_name }} tests
	mypy {{ cookiecutter.package_name }}
{%- if cookiecutter.docstring == 'Google' %}
	darglint {{ cookiecutter.package_name }}
{% endif %}

.PHONY: tests
tests:  ## Test your code.
	poetry run pytest tests/ --cov={{ cookiecutter.package_name }} --cov-report=term-missing:skip-covered --cov-report=xml

{%- if cookiecutter.python_client == 'y' %}
.PHONY: generate_client
generate_client:
	openapi-python-client --config client-config.yaml generate --url http://localhost:8000/openapi.json

.PHONY: update_client
update_client:
	openapi-python-client --config client-config.yaml update --url http://localhost:8000/openapi.json
{% endif %}
