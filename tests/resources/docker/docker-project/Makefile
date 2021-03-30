.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint:  ## Linter the code.
	isort docker_project tests --check
	flake8 docker_project tests
	mypy docker_project

.PHONY: tests
tests:  ## Test your code.
	poetry run pytest tests/ --cov=docker_project --cov-report=term-missing:skip-covered --cov-report=xml
