#!/bin/bash
source venv/bin/activate
pwd
ls -l
exec gunicorn 'run:app' -b:5000 --workers 2