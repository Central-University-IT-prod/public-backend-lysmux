from datetime import date

from pydantic import TypeAdapter

from resources_api.base_api import ApiClient
from .schemas import AirportCode, FlightTicket


class AirTicketsAPI(ApiClient):
    async def get_airport_code(self, city: str) -> AirportCode | None:
        response = await self._http_client.get(
            url="/tickets/air/airport_code?",
            params={
                "city": city
            }
        )
        if response.status_code != 200:
            return None
        return AirportCode.model_validate(response.json())

    async def get_tickets(
            self,
            from_airport: str,
            to_airport: str,
            departure_date: date,
            persons: int = 1
    ) -> list[FlightTicket]:
        response = await self._http_client.get(
            url="/tickets/air?",
            params={
                "from_airport": from_airport,
                "to_airport": to_airport,
                "departure_date": departure_date.isoformat(),
                "persons": persons,
            }
        )
        if response.status_code != 200:
            return []
        adapter = TypeAdapter(list[FlightTicket])
        return adapter.validate_python(response.json())
