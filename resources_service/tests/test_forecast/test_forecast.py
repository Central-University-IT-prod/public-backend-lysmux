from datetime import date

from starlette.testclient import TestClient


def test_forecast_good(client: TestClient):
    response = client.get(
        "/forecast?",
        params={
            "latitude": "59.959106",
            "longitude": "30.391215",
            "start_date": date.today().isoformat(),
            "end_date": date.today().isoformat(),
        }
    )
    assert response.status_code == 200


def test_forecast_bad(client: TestClient):
    response = client.get(
        "/forecast?",
        params={
            "latitude": "59.959106"
        }
    )
    assert response.status_code == 422
