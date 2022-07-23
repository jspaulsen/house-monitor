#!/bin/bash
set -ex

docker-compose \
    -f docker-compose.test.yaml \
    build 

docker-compose \
    -f docker-compose.test.yaml \
    run --rm \
    tests

results=$?

docker-compose \
    -f docker-compose.test.yaml \
    down

exit $results
