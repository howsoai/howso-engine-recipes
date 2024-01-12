#!/bin/bash
set -eux

# Install dependencies
install_deps() {
  python --version
  pip install -r requirements-${1}-dev.txt --user --no-deps
}

# Takes the cli params, and runs them, defaulting to 'help()'
if [ ! ${1:-} ]; then
help
else
"$@"
fi