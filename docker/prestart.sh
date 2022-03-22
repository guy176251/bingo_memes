#!/usr/bin/env bash

set -x

# until cd /app; do
#     echo "Waiting for server volume..."
#     sleep 2
# done

./manage.py migrate
./manage.py init_db

./manage.py collectstatic --noinput
cp -r /app/django_static /usr/share/nginx/html
./print-nginx-conf.sh >/etc/nginx/conf.d/custom.conf
