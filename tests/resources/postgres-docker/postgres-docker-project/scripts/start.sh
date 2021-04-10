#! /usr/bin/env bash


python scripts/wait_database.py


uvicorn "postgres_docker_project.main:app" --host "0.0.0.0" --port 8000

