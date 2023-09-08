#!/bin/bash
# Functions to archive and upload to artifactory the recipes file
# usage:  ./bin/build.sh release 2010.01.1
#
####

set -euo pipefail
# set -x
source config/build.properties

# Generate requirements.txt
# Requires pip-tools - `pip install pip-tools`
gen_requirements() {
  local pyversion=${1:-3.9}
  echo $pyversion
  rm -fv requirements-local-${pyversion}.txt
  # https://github.com/jazzband/pip-tools/issues/973 describes use of --allow-unsafe
  CUSTOM_COMPILE_COMMAND="./bin/build.sh gen_requirements $pyversion" pip-compile --upgrade requirements.in requirements-dev.in requirements-local.in --no-emit-index-url --resolver=backtracking --allow-unsafe --output-file requirements-local-${pyversion}.txt
}

# Gets the latest version of a pacakge and pins it in the requirements file
force_latest_package() {
  local package=${1}
  local req_file=${2:-requirements-local.in}
  local latest_version=$(pip install --use-deprecated=legacy-resolver ${package}== 2>&1 | grep -oE '(\(.*\))' | awk -F: '{print$NF}' | sed -E 's/( |\))//g' | tr ',' '\n' | tail -n 1)
  echo "Latest version of ${package} is ${latest_version}"
  # Check not 'none'
  if [ "${latest_version}" == "none" ]; then
    echo "ERROR: Could not find latest version of ${package}"
    exit 1
  fi
  sed -i "/${package}==/d" "${req_file}"
  sed -i "/${package}/d" "${req_file}"
  echo "${package}==${latest_version} # Added by automation - please leave" >> requirements-local.in
}

# Achieving two things here.
# 1) Forcing an upgrade, and a failure if we can't go to the latest - this is tricky to do just with pip-compile, and a unpinned package (-U will not fail if it can't upgrade)
# 2) Allowing the backtracking resolver to work in a reasonable time, with no version range, it will download all versions
pin_local_requirements() {
   force_latest_package howso-engine requirements-local.in
}

# Create a zip file with the recipes for uploading
archive() {
  local version=${1}
  local archive_file=${archive_prefix}-${version}.zip
  rm -f target/$archive_file
  mkdir -p target
  zip -r target/${archive_file} ./ -x 'README-dev.md' -x 'requirements-*.in' 'requirements*.txt' -x "pip.conf" -x 'target/*' -x "*/__pycache__/*" -x "/__pycache__/*" -x '__init__.py' -x '*.git*' -x 'junit' -x '*flake8' -x '*.direnv*' -x '*ipynb_checkpoints*' -x '*.envrc' -x 'Jenkinsfile*' -x '*bin*' -x '*.vscode*' -x '*__pycache__*' -x '*.pytest_cache*' -x 'tests/*' -x 'dumps/*' -x 'config/*' -x 'diveplane.yml*'
  echo "archive file: target/${archive_file}"
}

# Clear out all the stuff from testing, etc
clean() {
   rm -f *.trace
   rm -rf traces
   rm -f *rounds.txt
   rm -rf cucumber junit target html
   find ./ -name .pytest_cache -type d | xargs -rt rm -r
   find ./ -name __pycache__ -type d | xargs -rt rm -r
}

# Use jf cli to upload release to artifactory
upload(){
  local version=${1}
  local archive_file=${archive_prefix}-${version}.zip
  echo "About to upload ${archive_file} to artifactory - this will overwrite any existing release"
  read -p $'\e[33mAre you sure? (y/n)\e[0m' -n 1 -r
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
     jf rt u --spec config/jf-upload-recipe.spec --spec-vars "release=${version}"
  else
    exit 4
  fi
}

# Run pytest
test() {
  local loglevel=${1:-INFO}
  export HOWSO_CONFIG=${HOWSO_CONFIG:-$(readlink -f ./config/latest-mt-howso.yml)}
  cat $HOWSO_CONFIG
  pip list | grep ^diveplane
  time DIVEPLANE_EULA_ACCEPTED=True python -m pytest -s --log-cli-level=${loglevel} -o junit_family=xunit2 --junitxml=junit/test-results.xml
}

# Archive and upload
release(){
  local version=${1}
  archive ${version}
  upload ${version}
}


# Install dependencies
install_deps() {
  local pyversion=${1}
  echo "Installing dependencies for python version ${pyversion}"
  pip install --prefer-binary -r requirements-local-${pyversion}.txt
}


# Show usage, and print functions
help() {
  echo "usage: ./bin/build.sh <build-function> {params}"
  echo " where <build-function> one of :-"
  IFS=$'\n'
  for f in $(declare -F); do
    echo "    ${f:11}"
  done
}

# Takes the cli params, and runs them, defaulting to 'help()'
if [ ! ${1:-} ]; then
  help
else
  "$@"
fi