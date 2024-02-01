#!/bin/bash

# Get the GitHub PAT from the environment variable
GITHUB_PAT=${GITHUB_PAT}

# Construct the URL for your private repository
REPO_URL="https://${GITHUB_PAT}@github.com/neutrino-ai/neutrino-lib/tarball/main#egg=neutrino-lib"

# Install the private repo along with other dependencies
pip install ${REPO_URL} --upgrade
