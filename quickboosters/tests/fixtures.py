from __future__ import absolute_import

from typing import Generator

from flask import Flask
from flask.testing import FlaskClient

from flask_sqlalchemy import SQLAlchemy

from quickboosters import create_app

import pytest


@pytest.fixture()
def app() -> Flask:
    return create_app("development")


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def db(app: Flask) -> Generator[SQLAlchemy, None, None]:
    from quickboosters import db

    with app.app_context():
        db.drop_all()
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()