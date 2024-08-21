from starlette.testclient import TestClient


def test_route_good(client: TestClient):
    response = client.get(
        "/route?",
        params={
            "from_latitude": 59.959106,
            "from_longitude": 30.391215,
            "to_latitude": 59.895171,
            "to_longitude": 30.329073,
        }
    )
    assert response.status_code == 200


def test_route_bad_params(client: TestClient):
    response = client.get(
        "/route?",
    )
    assert response.status_code == 422
