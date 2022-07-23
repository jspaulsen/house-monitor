#!/bin/bash
set -ex

VERSION=$(cat VERSION)
source docker.env

source build.sh
docker push "${DOCKER_REPO}/${DOCKER_IMAGE}:${VERSION}"
