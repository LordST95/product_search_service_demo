#!/bin/bash

cd /project/src
python manage.py migrate
python manage.py runserver
