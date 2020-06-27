from . import client


def test_index(client):
    rv = client.get("/")
    assert b"<h1>Hello, world!</h1>" in rv.data
