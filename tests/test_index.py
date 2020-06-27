from . import client


def test_index(client):
    rv = client.get("/")
    assert b'{"hello":"Hello, World!"}\n' in rv.data
