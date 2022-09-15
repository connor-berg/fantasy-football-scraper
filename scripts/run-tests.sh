#!/usr/bin/env bash

set -o errexit
set -o verbose

# Run tests and measure code coverage (https://coverage.readthedocs.io)
PYTHONPATH="${PWD}/setup_statistics/src:${PWD}/collect_statistics/src" coverage run --source "${PWD}" --omit "tests/*" -m pytest tests
