#!/bin/bash

python manage.py makemigrations  --settings=core.settings.$MODE
python manage.py migrate  --settings=core.settings.$MODE

python manage.py create_superuser --settings=core.settings.$MODE

python manage.py collectstatic --clear --no-input  --settings=core.settings.$MODE

gunicorn --access-logfile /log/gunicorn/access.log \
         --error-logfile /log/gunicorn/error.log \
          core.wsgi:application \
          -b 0.0.0.0:8000


