import os, sys, uuid

SECRET_KEY = uuid.uuid4().bytes
DEBUG=True

HOSTNAME = 'http://127.0.0.1:5000'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#EXPLAIN_TEMPLATE_LOADING = True

# database_server
SQLALCHEMY_DATABASE_URI = 'sqlite:///database/boost.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True