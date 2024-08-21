from pydantic import TypeAdapter

from resources_api.base_api import ApiClient
from .schemas import Place


class PlacesAPI(ApiClient):
    async def suggest_attractions(
            self,
            longitude_min: float,
            longitude_max: float,
            latitude_min: float,
            latitude_max: float
    ) -> list[Place]:
        response = await self._http_client.get(
            url="/places/suggest_attractions?",
            params={
                "longitude_min": longitude_min,
                "longitude_max": longitude_max,
                "latitude_min": latitude_min,
                "latitude_max": latitude_max,
            }
        )
        if response.status_code != 200:
            return []
        adapter = TypeAdapter(list[Place])
        return adapter.validate_python(response.json())

    async def suggest_hotels(
            self,
            longitude_min: float,
            longitude_max: float,
            latitude_min: float,
            latitude_max: float
    ) -> list[Place]:
        response = await self._http_client.get(
            url="/places/suggest_hotels?",
            params={
                "longitude_min": longitude_min,
                "longitude_max": longitude_max,
                "latitude_min": latitude_min,
                "latitude_max": latitude_max,
            }
        )
        if response.status_code != 200:
            return []
        adapter = TypeAdapter(list[Place])
        return adapter.validate_python(response.json())

    async def suggest_caterings(
            self,
            latitude: float,
            longitude: float,
            radius: int = 1000
    ) -> list[Place]:
        response = await self._http_client.get(
            url="/places/suggest_caterings?",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "radius": radius
            }
        )
        if response.status_code != 200:
            return []
        adapter = TypeAdapter(list[Place])
        return adapter.validate_python(response.json())
