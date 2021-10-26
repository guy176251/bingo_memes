#!/usr/bin/env bash
# Executed in /app

set -x

init_db_success() {
    ./manage.py collectstatic --noinput
    cp -r /app/django_static /usr/share/nginx/html
}

init_db_failure() {
    local err=$?
    echo " -> backend ded, here problem: Status code: $err"
}

init_dev_db() {
    echo 'Creating test database...'
    ./manage.py init_db && init_db_success || init_db_failure
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

    #test -z "$DEBUG" && DEBUG=1
    DEBUG=${DEBUG:-1}
    test $DEBUG -eq 1 && init_dev_db

    ./print-nginx-conf.sh >/etc/nginx/conf.d/custom.conf
}

main
