from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from quickboosters.src.config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    config = Config()
    app.config.from_object(config)
    db.init_app(app)
    return app
