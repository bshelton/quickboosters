import pytest
from quickboosters import create_app


@pytest.fixture
def app():
    app = create_app('development')
    return app
