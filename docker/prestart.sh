#!/usr/bin/env bash

set -x

./manage.py migrate
./manage.py init_db

./print-nginx-conf.sh >/etc/nginx/conf.d/custom.conf
