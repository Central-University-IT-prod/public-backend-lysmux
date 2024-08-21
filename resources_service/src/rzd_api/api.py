from datetime import date

import faker
from cashews import noself, cache
from httpx import AsyncClient
from pydantic import TypeAdapter
from .schemas import RzdTicket, CityCode


class RzdAPI:
    def __init__(self) -> None:
        self._http_client = AsyncClient(
            headers={
                "User-Agent": faker.Faker().chrome(),
                "Content-Type": "application/json",
                "Accept-Language": "ru"
            }
        )

    @noself(cache)(ttl="7d")
    async def get_city_code(self, city: str) -> CityCode | None:
        response = await self._http_client.get(
            url="https://ticket.rzd.ru/api/v1/suggests?",
            params={
                "GroupResults": True,
                "RailwaySortPriority": True,
                "MergeSuburban": True,
                "Query": city,
                "Language": "ru",
                "TransportType": "rail",
            }
        )
        result = response.json()
        if not result:
            return None
        city_result = result["city"][0]
        return CityCode.model_validate(city_result)

    @noself(cache)(ttl="30m")
    async def get_tickets(
            self,
            from_station: str,
            to_station: str,
            departure_date: date
    ) -> list[RzdTicket]:
        response = await self._http_client.post(
            url="https://ticket.rzd.ru/apib2b/p/"
                "Railway/V1/Search/TrainPricing",
            json={
                "Origin": from_station,
                "Destination": to_station,
                "DepartureDate": departure_date.isoformat(),
                "GetTrainsFromSchedule": True,
                "CarGrouping": "DontGroup",
                "CarIssuingType": "All"
            }
        )
        ta = TypeAdapter(type=list[RzdTicket])
        return ta.validate_python(response.json()["Trains"])

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aenter__(self) -> "RzdAPI":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
