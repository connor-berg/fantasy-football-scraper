#!/usr/bin/env bash

set -o errexit
set -o verbose

poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --output requirements-dev.txt --dev

npx cdk deploy "$@"
