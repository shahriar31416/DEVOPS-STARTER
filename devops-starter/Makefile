.PHONY: help venv install test run build up down fmt lint

help:
	@echo "Common commands:"
	@echo "  make venv       - create venv"
	@echo "  make install    - install deps (dev)"
	@echo "  make test       - run tests"
	@echo "  make run        - run app locally"
	@echo "  make build      - docker build"
	@echo "  make up         - docker-compose up -d"
	@echo "  make down       - docker-compose down"

venv:
	python3 -m venv .venv

install: venv
	. .venv/bin/activate && pip install -r app/requirements.txt -r requirements-dev.txt

test:
	. .venv/bin/activate && pytest -q

run:
	. .venv/bin/activate && uvicorn app.main:app --reload

build:
	docker build -t devops-starter:local .

up:
	docker-compose up -d --build

down:
	docker-compose down
