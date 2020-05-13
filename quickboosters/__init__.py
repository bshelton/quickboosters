from flask import Flask, redirect, request
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from passlib.hash import sha256_crypt
from flask_socketio import SocketIO, send, emit, join_room

from quickboosters.config import ProductionConfig, DevConfig

db = SQLAlchemy()
socketio = SocketIO()

def create_app(environment):
    print(environment)
    app = Flask(__name__)
    if environment == "development":
        devconfig = DevConfig()
        app.config.from_object(devconfig)
        db.init_app(app)
        return app

def enable_extensions(app):
    Bootstrap(app)

def enable_login_mgr(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'userbp.login'

    from quickboosters.api.users.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def enable_models():
    from quickboosters.api.users import models
    from quickboosters.api.chat import models

def enable_routes():
    #To do
    from quickboosters.api.users import routes

def register_blueprints(app):
    from quickboosters.api.users import auth
    app.register_blueprint(auth)

def testas():
    return 'test'