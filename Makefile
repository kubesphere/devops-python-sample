PORT ?= 8080
IMAGE_NAME := python-server:latest
CONTAINER_NAME := python-server

.PHONY: run test build docker-build docker-run stop clean

run:
	python3 server.py

test:
	@echo "Starting server on port $(PORT)..."
	@( \
		set -e; \
		python3 server.py & SERVER_PID=$$!; \
		trap "kill -9 $$SERVER_PID 2>/dev/null || true" EXIT; \
		sleep 1; \
		echo "Testing / endpoint..."; \
		curl -s -o /dev/null -w "%{http_code}" http://localhost:$(PORT)/ | grep -q '^200$$'; \
		echo "Testing /health endpoint..."; \
		curl -s http://localhost:$(PORT)/health | grep -q '"status":"ok"'; \
		echo "Smoke tests passed."; \
	)

build:
	python3 -m py_compile server.py
	@echo "Build check passed."

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run -d --rm --name $(CONTAINER_NAME) -e PORT=$(PORT) -p $(PORT):$(PORT) $(IMAGE_NAME)

stop:
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME) 2>/dev/null || true

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete 2>/dev/null || true
