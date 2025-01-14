#!/bin/sh
echo "Starting static files..."
python manage.py makemigrations --noinput
echo "Migrations files collected."

echo "Starting migrations..."
python manage.py migrate --noinput
echo "Migrations completed."

echo "Starting createsuperuser..."
python manage.py shell < create_superuser.py
echo "CreateSuperUser completed."

echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Static files collected."

echo "Starting Gunicorn server..."
gunicorn base.wsgi:application -c gunicorn.conf.py