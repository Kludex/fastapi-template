
PARENTDIR := $(abspath $(dir $(abspath $(dir $$PWD))))

.PHONY: simple
simple:
	if [ -d simple/simple-project ]; then rm -Rf simple/simple-project; fi
	cookiecutter "${PARENTDIR}" --output-dir simple --config-file simple/config.yaml --no-input

.PHONY: test
tests:
	pytest simple/simple-project
