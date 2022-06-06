#!/bin/bash
set -ex


VERSION=$(cat VERSION)

source docker.env


docker build -t "${DOCKER_REPO}/${DOCKER_IMAGE}:${VERSION}" .
