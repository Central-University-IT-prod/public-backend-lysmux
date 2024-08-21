from starlette.testclient import TestClient


def test_suggest_caterings_good(client: TestClient):
    response = client.get(
        "/places/suggest_caterings?",
        params={
            "latitude": 59.959106,
            "longitude": 30.391215
        }
    )
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_suggest_caterings_bad_params(client: TestClient):
    response = client.get(
        "/places/suggest_caterings?",
    )
    assert response.status_code == 422
