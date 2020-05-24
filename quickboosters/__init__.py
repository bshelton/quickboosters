from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_mail import Mail

from quickboosters.config import DevConfig

db: SQLAlchemy = SQLAlchemy()


def create_app(environment):
    print(environment)
    app = Flask(__name__)
    if environment == "development":
        devconfig = DevConfig()
        app.config.from_object(devconfig)
        db.init_app(app)
        with app.app_context():
            enable_extensions(app)
            enable_login_mgr(app)
            register_blueprints(app)
        return app


def enable_extensions(app: Flask):
    CORS(app)


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
    app.register_blueprint(auth)
