PARENTDIR := $(abspath $(dir $(abspath $(dir $$PWD))))

.PHONY: tests
tests:
	pytest tests
	pytest examples/simple/simple-project/tests


.PHONY: test_suite
test_suite:
	cookiecutter . --output-dir ${path} --config-file ${path}/config.yaml --no-input
