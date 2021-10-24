#!/bin/sh

until cd /app; do
    echo "Waiting for server volume..."
    sleep 2
done

until poetry run ./manage.py migrate; do
    echo "Waiting for db to be ready..."
    sleep 2
done

poetry run ./manage.py init_db
init_db_status=$?

if test $init_db_status -eq 0; then
    poetry run ./manage.py collectstatic --noinput
    poetry run ./manage.py runserver 0.0.0.0:8000
    #poetry run gunicorn backend.wsgi --bind 0.0.0.0:8000 #--workers 4 --threads 4
else
    echo "Can't run backend: Status code $init_db_status"
fi

#####################################################################################
# Options to DEBUG Django server
# Optional commands to replace abouve gunicorn command

# Option 1:
# run gunicorn with debug log level
# gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 1 --log-level debug

# Option 2:
# run development server
# DEBUG=True ./manage.py runserver 0.0.0.0:8000
