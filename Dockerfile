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

FROM tiangolo/uwsgi-nginx:python3.10-2021-10-26

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install poetry
COPY ./backend/poetry.lock ./backend/pyproject.toml ./
RUN poetry export --without-hashes | pip install -r /dev/stdin

# copy backend
COPY ./backend ./

#RUN apt-get update && \
#    apt-get  --only-upgrade install -y libc6


# tests
#RUN mypy .
#RUN flake8 .

# copy frontend static files 
RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/build /usr/share/nginx/html
RUN ./manage.py collectstatic --noinput
RUN cp -r /app/django_static /usr/share/nginx/html

# Copy docker image related files
COPY ./docker/prestart.sh ./
COPY ./docker/print-nginx-conf.sh ./
COPY ./docker/uwsgi.ini ./
