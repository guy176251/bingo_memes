### Stage 1: build ###

FROM node:16.11.1-alpine as builder

# Set working directory.
WORKDIR /app

# Copy app dependencies.
COPY ./frontend/package.json ./frontend/package-lock.json ./

# Install app dependencies.
RUN npm install

# Copy app files.
#COPY ./frontend ./
COPY ./frontend/public ./public
COPY ./frontend/src ./src
COPY ./frontend/tsconfig.json ./

# Build app
RUN npm run build


### Stage 2: delivery ###

#FROM nginx:1.15.7-alpine
FROM nginx:1.21.3-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image.
COPY --from=builder /app/build /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./docker/frontend/nginx/nginx.conf /etc/nginx/conf.d/default.conf
