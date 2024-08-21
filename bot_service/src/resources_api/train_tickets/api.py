from datetime import date

from pydantic import TypeAdapter

from resources_api.base_api import ApiClient
from .schemas import CityCode, RzdTicket


class TrainTicketsAPI(ApiClient):
    async def get_city_code(self, city: str) -> CityCode | None:
        response = await self._http_client.get(
            url="/tickets/train/city_code?",
            params={
                "city": city
            }
        )
        if response.status_code != 200:
            return None
        return CityCode.model_validate(response.json())

    async def get_tickets(
            self,
            from_station: str,
            to_station: str,
            departure_date: date
    ) -> list[RzdTicket]:
        response = await self._http_client.get(
            url="/tickets/train?",
            params={
                "from_station": from_station,
                "to_station": to_station,
                "departure_date": departure_date.isoformat()
            }
        )
        if response.status_code != 200:
            return []
        adapter = TypeAdapter(list[RzdTicket])
        return adapter.validate_python(response.json())
