from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_cors import CORS

from quickboosters.environments import Environment
from quickboosters.config import DevConfig, TestConfig

db: SQLAlchemy = SQLAlchemy()
socketio = SocketIO()


def create_app(env: Environment) -> Flask:
    app = Flask(__name__)
    if env.name == "DEVELOPMENT":
        print(env.name)
        devconfig = DevConfig()
        app.config.from_object(devconfig)
        db.init_app(app)
        socketio.init_app(app)
        with app.app_context():
            enable_extensions(app)
            enable_login_mgr(app)
            register_blueprints(app)
    elif env.name == "TESTING":
        testconfig = TestConfig()
        app.config.from_object(testconfig)
        return app
    return app


def enable_extensions(app: Flask):
    CORS(app)


def enable_socketio(app: Flask):
    socketio = SocketIO(app, async_mode=None)
    return socketio


def enable_login_mgr(app: Flask):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'userbp.login'

    from quickboosters.api.users.model import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    from quickboosters.api.users.controller import auth
    from quickboosters.api.chat import chat
    app.register_blueprint(auth)
    app.register_blueprint(chat)
