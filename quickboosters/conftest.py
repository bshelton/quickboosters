import os

import pytest

from quickboosters import create_app, db as _db
from quickboosters import DevConfig


@pytest.fixture(scope='session')
def app(request):
    app = create_app('development')
    devconfig = DevConfig()
    app.config.from_object(devconfig)
    app.app_context().push()
    _db.init_app(app)
    _db.create_all()

    @request.addfinalizer
    def teardown():
        _db.drop_all()
    return app


@pytest.fixture(scope='session')
def db(app, request):

    with app.app_context():
        _db.drop_all()
        _db.create_all()

    @request.addfinalizer
    def teardown():
        _db.drop_all()
    return _db
