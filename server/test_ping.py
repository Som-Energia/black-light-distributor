import os
import tempfile
import pytest
from . import build_app

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    apptest = build_app(db_path)

    with apptest.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def testPingEndpoint(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json == "pong!"