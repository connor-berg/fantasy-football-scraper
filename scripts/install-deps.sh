#!/usr/bin/env bash

set -o errexit
set -o verbose

# Install local CDK CLI version
npm install

# Install project dependencies
pip install -r requirements.txt -r collect_statistics/src/requirements.txt -r requirements-dev.txt
