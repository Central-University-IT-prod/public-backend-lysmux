from starlette.testclient import TestClient


def test_coordinates_good(client: TestClient):
    response = client.get(
        "/location/from_coordinates?",
        params={
            "latitude": 59.959106,
            "longitude": 30.391215,
        }
    )
    assert response.status_code == 200


def test_coordinates_bad_params(client: TestClient):
    response = client.get(
        "/location/from_coordinates?",
        params={
            "latitude": 1111.1111,
            "longitude": 1111.1111,
        }
    )
    assert response.status_code == 422
