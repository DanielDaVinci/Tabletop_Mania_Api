#!/bin/bash

python3 -m venv venv
source ./venv/bin/activate
#satisfying requirements
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply database migrations
sleep 7
echo "Apply database migrations"
python manage.py migrate

python manage.py createimmortaluser

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8080