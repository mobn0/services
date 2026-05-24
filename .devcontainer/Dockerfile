FROM mcr.microsoft.com/devcontainers/python:3.12

COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/tmp/services-venv

COPY backend/pyproject.toml backend/uv.lock ./

RUN uv sync  --locked --no-dev --no-install-project --verbose --no-cache


RUN apt-get update && apt-get install -y \
    curl