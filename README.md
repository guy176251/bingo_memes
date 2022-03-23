# Bingo Memes

This is the repo for the [Bingo Memes](http://dev.bingomemes.com) website. This site utilizes [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/) for the backend and [React](https://reactjs.org/) + [Typescript](https://www.typescriptlang.org/) for the frontend. The site minus the database is contained within a single Docker image.

## Environment Variables

These are the environment variables understood by the container image. Unless explicitly stated, variables don't have a default value.

| Variable | Description | Default Value |
|---|---|---|
| `SERVER_NAME` | Sets `server_name` in the generated `custom.conf` in `/etc/nginx/conf.d/`. |`_`|
| `DEBUG` | Corresponds to the equivalent variable in `/backend/backend/settings.py`. Also used to set the debug state of other parts of the site. |`1`|
| `SECRET_KEY` | Corresponds to the equivalent variable in `/backend/backend/settings.py`. |
| `ALLOWED_HOSTS` | Corresponds to the equivalent variable in `/backend/backend/settings.py`. Each host must be separated by any number of spaces. |
| `DB_USER` | Database username. |
| `DB_PASSWORD` | Database password. |
| `DB_NAME` | Database name. |
| `DB_HOST` | Database host. |
| `DB_PORT` | Database port. |
| `DJANGO_SUPERUSER_USERNAME` | Built-in Django variable. Needed for automated superuser creation. |
| `DJANGO_SUPERUSER_EMAIL` | Built-in Django variable. Needed for automated superuser creation. |
| `DJANGO_SUPERUSER_PASSWORD` | Built-in Django variable. Needed for automated superuser creation. |
