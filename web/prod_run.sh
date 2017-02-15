#!/bin/bash

/usr/bin/python3.5 /data/web/harchenkopro/manage.py makemigrations
/usr/bin/python3.5 /data/web/harchenkopro/manage.py migrate
/usr/bin/python3.5 /data/web/harchenkopro/manage.py collectstatic
/usr/bin/python3.5 /data/web/harchenkopro/manage.py loaddata /data/web/db.json