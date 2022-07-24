#!/bin/bash
set -ex

VERSION=$(cat VERSION)
source docker.env


docker buildx \
    build \
    --platform linux/amd64,linux/arm64 \
    --target ${TARGET} \
    -t "${DOCKER_REPO}/${DOCKER_IMAGE}:${VERSION}" \
    --push \
    .
