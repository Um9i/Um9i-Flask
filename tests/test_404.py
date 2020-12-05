from . import client


def test_404(client):
    rv = client.get("/randomurl")
    assert b"<h1 class="text-muted text-center py-5">404: Page Not Found</h1>" in rv.data
