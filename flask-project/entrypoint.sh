#!/usr/bin/env bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py bulk
python app.py