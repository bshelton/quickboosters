from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
import os
import sys
from dotenv import load_dotenv

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
    from quickboosters.config import DevConfig
    from quickboosters.config import Config
    from quickboosters.backend.users.dev import sample_data
    print(Config().project_folder)
    print(DevConfig().verbose())
    app = create_app('development')
    app.app_context().push()
    sample_data.create_user()
else:
    app = create_app('prod')

enable_extensions(app)
enable_login_mgr(app)
enable_models()
enable_routes()
manager = Manager(app)
register_blueprints(app)

db.create_all(app=app)