#!/bin/bash
set -ex


VERSION=$(cat VERSION)

source docker.env


docker push "${DOCKER_REPO}/${DOCKER_IMAGE}:${VERSION}"
