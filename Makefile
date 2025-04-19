.PHONY: test

DOCKER_SERVICE ?= tposts
TEST_PATH ?= src
MANAGE_PY := src/manage.py

ifeq ($(LOCAL), true)
	PYTHON ?= poetry run python
	RUNNING_MODE ?= locally
else
	PYTOHN ?= docker compose up exec poetry run python
	RUNNING_MODE ?= in Docker
endif

## Run the test suite
test:
	echo "Running test $(RUNNING_MODE)"
	$(PYTHON) $(MANAGE_PY) test $(TEST_PATH); \


