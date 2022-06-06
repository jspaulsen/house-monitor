FROM python:3.10.4-slim-buster

ARG DBMATE_VERSION=v1.15.0
ENV DBMATE_URL=https://github.com/amacneil/dbmate/releases/download/${DBMATE_VERSION}/dbmate-linux-amd64

ARG USER_UID=1000
ARG USER_GID=$USER_UID


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
    curl -fsSL -o /usr/local/bin/dbmate ${DBMATE_URL} && \
    chmod +x /usr/local/bin/dbmate


USER app
WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN \
    pipenv sync


COPY . /app/

ENTRYPOINT [ "bin/docker_bootstrap"]
CMD ["production"]
