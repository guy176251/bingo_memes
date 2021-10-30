#!/usr/bin/env bash
# Executed in /app

set -x

until cd /app; do
    echo "Waiting for server volume..."
    sleep 2
done

until ./manage.py makemigrations; do
    echo "Waiting for db to be ready..."
    sleep 2
done

./manage.py migrate

#test -z "$DEBUG" && DEBUG=1
DEBUG=${DEBUG:-1}
test $DEBUG -eq 1 && ./manage.py init_db

./manage.py collectstatic --noinput
cp -r /app/django_static /usr/share/nginx/html
./print-nginx-conf.sh >/etc/nginx/conf.d/custom.conf
