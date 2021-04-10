#! /usr/bin/env bash



uvicorn "docker_project.main:app" --host "0.0.0.0" --port 8000

