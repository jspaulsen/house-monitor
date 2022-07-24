# syntax=docker/dockerfile:1.2
FROM python:3.10.4-slim-buster as production

ARG DBMATE_VERSION=v1.15.0
ARG TARGETPLATFORM
ENV DBMATE_URL=https://github.com/amacneil/dbmate/releases/download/${DBMATE_VERSION}/dbmate-linux

ARG USER_UID=1000
ARG USER_GID=$USER_UID

SHELL ["/bin/bash", "-c"]


RUN \
    apt-get update && \
    apt-get install -y \
        gcc \
        python-dev \
        libpq-dev \
        curl && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install \
        pipenv && \
    useradd \
        --home-dir /app \
        --create-home \
        app

RUN \
    if [[ ${TARGETPLATFORM} == *"arm"* ]]; then ARCH="arm64"; else ARCH="amd64"; fi && \
    curl -fsSL -o /usr/local/bin/dbmate "${DBMATE_URL}-${ARCH}" && \
    chmod +x /usr/local/bin/dbmate


USER app
WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN \
    pipenv sync

COPY bin /app/bin
COPY db /app/db
COPY VERSION /app/
COPY app /app/app

ENTRYPOINT [ "bin/docker_bootstrap"]
CMD ["production"]


################
FROM production as test

RUN \
    pipenv install --dev

COPY tests /app/tests
