
from starlette.testclient import TestClient


def test_search_good(client: TestClient):
    response = client.get(
        "/location/search?",
        params={
            "query": "Москва"
        }
    )
    assert response.status_code == 200


def test_search_unknown_query(client: TestClient):
    response = client.get(
        "/location/search?",
        params={
            "query": "ABCDEFGHJKLAIS"
        }
    )
    assert response.status_code == 404


def test_search_bad_params(client: TestClient):
    response = client.get(
        "/location/search?"
    )
    assert response.status_code == 422
