import pytest
import flask


@pytest.fixture(scope="module")
def app():
    a = flask.Flask('collar_metrics')
    return a


@pytest.fixture(scope="module")
def api_client(app):
    app.testing = True
    return app.test_client()


def test_get_no_barks(api_client):
    response = api_client.get("/collar/1/barks")
    assert response.
