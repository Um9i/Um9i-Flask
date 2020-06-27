import pytest
from project import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert b'{"hello":"Hello, World!"}\n' in rv.data
