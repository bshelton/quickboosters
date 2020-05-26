#!/bin/bash
source venv/bin/activate
pwd
ls -l
exec gunicorn 'run:create_app()' -b:8000 --workers 2