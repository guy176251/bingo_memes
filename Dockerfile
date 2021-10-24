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
ENV APP_MODULE backend.wsgi

# install dependencies
COPY ./backend/poetry.lock ./backend/pyproject.toml .
RUN pip install poetry
#RUN poetry install --no-dev
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copy backend
COPY ./backend ./
#COPY ./docker /docker
#RUN poetry run flake8 .

# copy frontend static files 
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/build /usr/share/nginx/html

# Copy nginx configuration
COPY ./docker/frontend/nginx/nginx.conf /etc/nginx/conf.d/custom.conf

# Copy prestart script
COPY ./docker/backend/prestart.sh /app

# Copy uwsgi.ini
COPY ./docker/backend/uwsgi.ini /app
