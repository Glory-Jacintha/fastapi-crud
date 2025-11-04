import pytest
from stralette.testclient import TestClient

from app.main import app

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client #testing happens here

