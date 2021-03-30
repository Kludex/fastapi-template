.PHONY: tests
tests:
	pytest tests


.PHONY: test_suite
test_suite:
	cookiecutter . --output-dir ${path} --config-file ${path}/config.yaml --no-input
