from datetime import date

import faker
from cashews import noself, cache
from httpx import AsyncClient

from .schemas import FlightTicket, FlightSegment, AirportCode


class KupiBiletAPI:
    def __init__(self) -> None:
        self._http_client = AsyncClient(
            headers={
                "User-Agent": faker.Faker().chrome(),
                "Content-Type": "application/json",
                "Accept-Language": "ru",
                "x-requested-with": "XMLHttpRequest"
            }
        )

    @noself(cache)(ttl="7d")
    async def get_airport_code(self, city: str) -> AirportCode | None:
        response = await self._http_client.get(
            url="https://hinter.kupibilet.ru/hinter.json?",
            params={
                "str": city,
                "limit": 1
            }
        )
        result = response.json()["data"]
        if not result:
            return None
        return AirportCode(code=result[0]["city"]["code"])

    @noself(cache)(ttl="30m")
    async def get_tickets(
            self,
            from_airport: str,
            to_airport: str,
            departure_date: date,
            persons: int = 1
    ) -> list[FlightTicket]:
        response = await self._http_client.post(
            url="https://api-rs.kupibilet.ru/frontend_search",
            json={
                "trips": [
                    {
                        "arrival": to_airport,
                        "departure": from_airport,
                        "date": departure_date.isoformat()
                    }
                ],
                "travelers": {
                    "adult": persons,
                    "child": 0,
                    "infant": 0
                },
                "cabin": "economy",
                "agent": "context_nb",
                "language": "RU",
                "currency": "RUB",
                "client_platform": "web"
            }
        )
        tickets = []
        result = response.json()
        variants = result["variants"]
        flights = result["flights"]
        aircrafts = result["aircrafts"]
        airports = result["anyports"]
        cities = result["cities"]
        for variant in variants:
            price = variant["price"]["amount"]
            segments = []
            for flight_id in variant["segments"][0]["flights"]:
                flight = flights[flight_id]
                flight_number = flight["number"]
                flight_prefix = flight["marketing_carrier"]

                aircraft_code = flight["equipment"]
                aircraft = aircrafts[aircraft_code]
                aircraft_name = aircraft["name"]

                airport_from_code = flight["departure"]
                airport_from = airports[airport_from_code]
                airport_from_name = airport_from["name"]
                city_from_code = airport_from["city_code"]
                city_from = cities[city_from_code]
                city_from_name = city_from["name"]

                airport_to_code = flight["arrival"]
                airport_to = airports[airport_to_code]
                airport_to_name = airport_to["name"]
                city_to_code = airport_to["city_code"]
                city_to = cities[city_to_code]
                city_to_name = city_to["name"]

                departure_at = flight["departure_datetime"]
                arrival_at = flight["arrival_datetime"]

                company_code = flight["operating_carrier"]
                company = result["airlines"][company_code]
                company_name = company["name"]

                segments.append(FlightSegment(
                    aircraft=aircraft_name,
                    flight_number=f"{flight_prefix} {flight_number}",
                    company=company_name,

                    departure_airport_name=airport_from_name,
                    departure_airport_code=airport_from_code,
                    departure_city_name=city_from_name,

                    arrival_airport_name=airport_to_name,
                    arrival_airport_code=airport_to_code,
                    arrival_city_name=city_to_name,

                    departure_at=departure_at,
                    arrival_at=arrival_at,
                ))

            tickets.append(FlightTicket(
                price=price,
                segments=segments,
                buy_link=f"https://kupibilet.ru/mbooking/step0/{variant["id"]}"
            ))

        return tickets

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aenter__(self) -> "KupiBiletAPI":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
