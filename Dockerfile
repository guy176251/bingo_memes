### combine frontend and backend images into single image ###


### Stage 1: Frontend build ###

FROM node:16.11.1-alpine as builder
WORKDIR /app

# Install dependencies
COPY ./frontend/package.json ./frontend/package-lock.json ./frontend/tsconfig.json  ./
RUN npm install

# Build src
COPY ./frontend/public ./public
COPY ./frontend/src ./src
RUN npm run build


### Stage 2: Backend ###

FROM tiangolo/uwsgi-nginx:python3.9-2021-10-02

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install poetry
COPY ./backend/poetry.lock ./backend/pyproject.toml ./
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copy backend
COPY ./backend ./

# tests
RUN mypy .
RUN flake8 .

# copy frontend static files 
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/build /usr/share/nginx/html

# Copy docker image related files
COPY ./docker/prestart.sh ./
COPY ./docker/print-nginx-conf.sh ./
COPY ./docker/uwsgi.ini ./
