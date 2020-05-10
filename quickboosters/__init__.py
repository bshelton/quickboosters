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

    from quickboosters.backend.users.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from quickboosters.backend.booster.models import Booster
    def load_booster(booster_id):
        return Booster.query.get(int(booster_id))

def enable_models():
    from quickboosters.backend.users import models
    from quickboosters.backend.order import models
    from quickboosters.backend.booster import models
    from quickboosters.backend.admin import models
    from quickboosters.backend.chat import models


def enable_routes():
    from quickboosters.backend.users import routes
    from quickboosters.backend.order import routes
    from quickboosters.backend.booster import routes
    from quickboosters.backend.admin import routes
    from quickboosters.backend.chat import routes

def register_blueprints(app):
    from quickboosters.backend.admin.routes import adminbp
    from quickboosters.backend.order.routes import orderbp
    from quickboosters.backend.users.routes import userbp
    from quickboosters.backend.chat.routes import chatbp
    from quickboosters.backend.booster.routes import boosterbp
    from quickboosters.backend.routes import mainbp
    app.register_blueprint(mainbp)
    app.register_blueprint(orderbp)
    app.register_blueprint(userbp)
    app.register_blueprint(boosterbp)
    app.register_blueprint(adminbp)
    app.register_blueprint(chatbp)