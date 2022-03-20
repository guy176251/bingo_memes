#!/usr/bin/env bash

set -x

# if [ "$DJANGO_DB_USE_POSTGRES" = "1" ]
# then
#     echo "Waiting for postgres..."
# 
#     while ! nc -v -z 0.0.0.0 $DJANGO_DB_PORT; do
#       sleep 0.1
#     done
# 
#     echo "PostgreSQL started"
# fi

# until cd /app; do
#     echo "Waiting for server volume..."
#     sleep 2
# done

#./manage.py makemigrations --check
# sleep 10
./manage.py migrate

# DEBUG=${DEBUG:-0}
# if ! test $DEBUG -eq 0; then
#     ./manage.py init_db
# fi
#
# ./manage.py collectstatic --noinput
# cp -r /app/django_static /usr/share/nginx/html
./print-nginx-conf.sh >/etc/nginx/conf.d/custom.conf
