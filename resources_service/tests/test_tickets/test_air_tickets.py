from starlette.testclient import TestClient


def test_airport_code_good(client: TestClient):
    response = client.get(
        "/tickets/air/airport_code?",
        params={
            "city": "Москва",
        }
    )
    assert response.status_code == 200
    assert response.json()["code"] == "MOW"


def test_airport_code_bad(client: TestClient):
    response = client.get(
        "/tickets/air/airport_code?",
        params={
            "city": "asassasasas",
        }
    )
    assert response.status_code == 404


def test_tickets_air_good(client: TestClient):
    response = client.get(
        "/tickets/air?",
        params={
            "from_airport": "MOW",
            "to_airport": "LED",
            "departure_date": "2024-03-30"
        }
    )
    assert response.status_code == 200


def test_tickets_air_bad(client: TestClient):
    response = client.get(
        "/tickets/air?",
        params={
            "from_airport": "MOW",
            "to_airport": "LED",
            "departure_date": "2023-03-30"
        }
    )
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_tickets_air_bad_params(client: TestClient):
    response = client.get(
        "/tickets/air?",
    )
    assert response.status_code == 422
