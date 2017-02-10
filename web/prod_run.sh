#!/bin/bash

/usr/bin/python3.5 harchenkopro/manage.py makemigrations
/usr/bin/python3.5 harchenkopro/manage.py migrate
/usr/bin/python3.5 harchenkopro/manage.py collectstatic

gulp -d