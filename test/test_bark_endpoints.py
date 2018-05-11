import pytest
import flask
import json
import collar_metrics


def jsonapi(response_data):
    return json.loads(str(response_data, 'utf-8'))


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


def test_new_barks_are_preserved(api_client):
    bark_event = {"type": "barks", "attributes": {"volume": 5, "timestamp": "2018-01-01"}}
    api_client.post(
        "/collar/1/barks/new",
        data=json.dumps(dict(data=[bark_event])),
        content_type="application/json"
    )
    response = api_client.get("/collar/1/barks")
    assert jsonapi(response.data)['data'][-1] == bark_event
