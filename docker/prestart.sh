#!/usr/bin/env bash

set -x

until cd /app; do
    echo "Waiting for server volume..."
    sleep 2
done

# until ./manage.py makemigrations; do
#     echo "Waiting for db to be ready..."
#     sleep 2
# done

./manage.py makemigrations --check

DEBUG=${DEBUG:-0}
if ! test $DEBUG -eq 0; then
    ./manage.py init_db
fi

./manage.py migrate

./manage.py collectstatic --noinput
cp -r /app/django_static /usr/share/nginx/html
./print-nginx-conf.sh >/etc/nginx/conf.d/custom.conf
