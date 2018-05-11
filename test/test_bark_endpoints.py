import pytest
import flask
import json
import collar_metrics


@pytest.fixture(scope="module")
def app():
    a = flask.Flask('collar_metrics')
    collar_metrics.bootstrap(a)
    return a


@pytest.fixture(scope="module")
def api_client(app):
    app.testing = True
    return app.test_client()


def test_get_barks_200(api_client):
    response = api_client.get("/collar/1/barks")
    assert response.status_code == 200


def test_get_barks_empty(api_client):
    response = api_client.get("/collar/1/barks")
    assert not jsonapi(response.data)['data']


def test_posting_adds_a_bark(api_client):
    api_client.post(
        "/collar/1/barks/new",
        data=json.dumps(dict(blah="crap")),
        content_type="application/json"
    )
    response = api_client.get("/collar/1/barks")
    assert len(jsonapi(response.data)['data']) == 1

def jsonapi(response_data):
    return json.loads(str(response_data, 'utf-8'))
