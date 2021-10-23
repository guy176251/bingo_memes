#!/usr/bin/env bash

set -x

init_success() {
    ./manage.py collectstatic --noinput
    cp -r /app/django_static /usr/share/nginx/html
}

init_failure() {
    local err=$?
    echo " -> backend ded, here problem: Status code: $err"
}

main() {
    until cd /app; do
        echo "Waiting for server volume..."
        sleep 2
    done

    until ./manage.py migrate; do
        echo "Waiting for db to be ready..."
        sleep 2
    done

    ./manage.py init_db && init_success || init_failure
}

main
