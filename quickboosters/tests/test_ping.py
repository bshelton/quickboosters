import json

from quickboosters.tests.fixtures import app


def test_ping(app):
    client = app.test_client()
    resp = client.get('/index')
    assert resp.status_code == 200
