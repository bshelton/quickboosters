from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys
from dotenv import load_dotenv
from quickboosters.config import DevConfig
from quickboosters.api.users.dev.sample_data import create_user
from quickboosters.api.users.dev.sample_data import create_order
from quickboosters import (
    create_app,
    db,
    socketio,
    enable_extensions,
    enable_login_mgr, 
    enable_models, 
    enable_routes,
    register_blueprints
)

conf = os.getenv('FLASK_ENV')

if conf == 'development':
    print(DevConfig().verbose())
    app = create_app('development')
    app.app_context().push()
    db.create_all(app=app)
    create_order()
else:
    app = create_app('prod')

enable_extensions(app)
enable_login_mgr(app)
enable_models()
enable_routes()
register_blueprints(app)

