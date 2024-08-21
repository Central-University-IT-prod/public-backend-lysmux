from pydantic import TypeAdapter

from resources_api.base_api import ApiClient
from .schemas import Location


class LocationAPI(ApiClient):
    async def search(self, query: str) -> Location:
        response = await self._http_client.get(
            url="/location?",
            params={
                "query": query
            }
        )
        return Location.model_validate(response.json())

    async def suggest(self, query: str) -> list[Location]:
        response = await self._http_client.get(
            url="/location/suggest?",
            params={
                "query": query
            }
        )
        if response.status_code != 200:
            return []
        adapter = TypeAdapter(list[Location])
        return adapter.validate_python(response.json())

    async def from_coordinates(
            self,
            latitude: float,
            longitude: float,
            city: bool = False,
    ) -> Location:
        response = await self._http_client.get(
            url="/location/from_coordinates?",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "city": city
            }
        )
        return Location.model_validate(response.json())
