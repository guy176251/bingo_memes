# slim image ends up being smaller bc
# alpine needs a lot of extra deps
FROM python:3.9-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy poetry files
COPY ./backend/poetry.lock ./backend/pyproject.toml .

# install dependencies
RUN pip install poetry
RUN poetry install --no-dev

# copy project
COPY ./backend ./
COPY ./docker /docker
#RUN poetry run flake8 .
