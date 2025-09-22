FROM python:3.12.11-slim-bookworm

ARG POETRY_VERSION=2.1.1

WORKDIR /app

COPY . .

RUN curl -sSL https://install.python-poetry.org | python3 -


WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]