import os, sys, uuid

SECRET_KEY = uuid.uuid4().bytes
DEBUG=True

HOSTNAME = 'http://127.0.0.1:5000'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# database_server
SQLALCHEMY_DATABASE_URI = 'sqlite:///c:\\Users\\Brock\\Desktop\\quickboosters\\rami.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True