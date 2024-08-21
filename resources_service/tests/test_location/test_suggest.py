
from starlette.testclient import TestClient


def test_suggest_good(client: TestClient):
    response = client.get(
        "/location/suggest?",
        params={
            "query": "Москва"
        }
    )
    assert response.status_code == 200


def test_suggest_unknown_query(client: TestClient):
    response = client.get(
        "/location/suggest?",
        params={
            "query": "ABCDEFGHJKLAIS"
        }
    )
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_suggest_bad_params(client: TestClient):
    response = client.get(
        "/location/suggest?"
    )
    assert response.status_code == 422
