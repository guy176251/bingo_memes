### combine frontend and backend images into single image ###


### Stage 1: Frontend build ###

FROM node:16.11.1-alpine as builder
WORKDIR /app

# Install dependencies
COPY ./frontend/package.json ./frontend/yarn.lock ./frontend/tsconfig.json  ./
RUN yarn install

# Build src
COPY ./frontend/public ./public
COPY ./frontend/src ./src
RUN yarn run build


### Stage 2: Backend ###

FROM tiangolo/uwsgi-nginx:python3.10-2021-10-26

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install poetry
COPY ./backend/poetry.lock ./backend/pyproject.toml ./
RUN poetry export --without-hashes | pip install -r /dev/stdin

# RUN apt update && apt install -y netcat

# copy backend
COPY ./backend ./

# tests
#RUN mypy --cache-dir=/dev/null .
#RUN flake8 .
#RUN pytest

# copy frontend static files 
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/build /usr/share/nginx/html

# Copy docker image related files
COPY ./docker/prestart.sh ./
COPY ./docker/print-nginx-conf.sh ./
COPY ./docker/uwsgi.ini ./

# collect and move django static files
RUN DJANGO_SECRET_KEY=placeholder ./manage.py collectstatic --noinput
RUN mv /app/django_static /usr/share/nginx/html
