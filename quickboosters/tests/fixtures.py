from __future__ import absolute_import
from typing import Generator

from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from quickboosters import create_app, db
from quickboosters.environments import Environment


import pytest


@pytest.fixture()
def app() -> Flask:
    app = create_app(Environment.TESTING)
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def db(app: Flask) -> Generator[SQLAlchemy, None, None]:
    from quickboosters import db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():

        db.drop_all()
        db.create_all()
        yield db
        db.session.close()
        db.drop_all()
        db.session.commit()
        db.session.close()
