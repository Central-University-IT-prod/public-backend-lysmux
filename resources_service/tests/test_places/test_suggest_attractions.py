from starlette.testclient import TestClient


def test_suggest_attractions_good(client: TestClient):
    response = client.get(
        "/places/suggest_attractions?",
        params={
            "latitude_max": 59.959106,
            "longitude_max": 30.391215,
            "latitude_min": 59.895171,
            "longitude_min": 30.329073,
        }
    )
    assert response.status_code == 200
    assert len(response.json()) != 0


def test_attractions_bad_params(client: TestClient):
    response = client.get(
        "/places/suggest_attractions?",
    )
    assert response.status_code == 422
