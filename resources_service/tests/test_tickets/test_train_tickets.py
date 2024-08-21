from starlette.testclient import TestClient


def test_city_code_good(client: TestClient):
    response = client.get(
        "/tickets/train/city_code?",
        params={
            "city": "Москва",
        }
    )
    assert response.status_code == 200
    assert response.json()["code"] == "2000000"


def test_city_cod_bad(client: TestClient):
    response = client.get(
        "/tickets/train/city_code?",
        params={
            "city": "asassasasas",
        }
    )
    assert response.status_code == 404


def test_tickets_train_good(client: TestClient):
    response = client.get(
        "/tickets/train?",
        params={
            "from_station": "2000000",
            "to_station": "2004000",
            "departure_date": "2024-03-30"
        }
    )
    assert response.status_code == 200


def test_tickets_train_bad(client: TestClient):
    response = client.get(
        "/tickets/train?",
        params={
            "from_station": "2000000",
            "to_station": "2004000",
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
