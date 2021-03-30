
.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: tests
tests: ## Run tests
	poetry run pytest tests/ --cov="{{ cookiecutter.project_slug }}" --cov-report=term-missing:skip-covered --cov-report=xml


.PHONY: test_suite
test_suite: ## Create a test suite using the configuration `path`
	cookiecutter . --output-dir ${path} --config-file ${path}/config.yaml --no-input
