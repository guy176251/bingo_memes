# slim image ends up being smaller bc
# alpine needs a lot of extra deps
FROM python:3.9-slim

# set work directory
WORKDIR /usr/app/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy poetry files
COPY poetry.lock pyproject.toml .

# install dependencies
RUN pip install poetry
RUN poetry install --no-dev

# copy project
COPY . .
#RUN poetry run flake8 .
