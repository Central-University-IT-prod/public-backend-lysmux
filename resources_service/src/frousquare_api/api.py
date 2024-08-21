from typing import Any

import httpx
from cashews import cache, noself

from .schemas import Place


class FourSquareAPI:
    def __init__(self, api_key: str) -> None:
        self._http_client = httpx.AsyncClient(
            base_url="https://api.foursquare.com/v3/places",
            headers={
                "accept": "application/json",
                "Authorization": api_key,
                "Accept-Language": "ru"
            },
            params={
                "fields": "fsq_id,"
                          "name,"
                          "location,"
                          "geocodes,"
                          "description,"
                          "rating,"
                          "price",
                "lang": "ru"
            }
        )

    @noself(cache)(ttl="3d")
    async def suggest_attractions(
            self,
            longitude_min: float,
            longitude_max: float,
            latitude_min: float,
            latitude_max: float,
            limit: int = 20
    ) -> list[Place]:
        response = await self._http_client.get(
            url="/search?",
            params={
                "sw": f"{latitude_min},{longitude_min}",
                "ne": f"{latitude_max},{longitude_max}",
                "categories": "16000",
                "sort": "RATING",
                "limit": limit
            }
        )
        if response.status_code != 200:
            return []
        raw_results = response.json()["results"]
        return list(map(self.json_to_schema, raw_results))

    @noself(cache)(ttl="3d")
    async def suggest_hotels(
            self,
            longitude_min: float,
            longitude_max: float,
            latitude_min: float,
            latitude_max: float,
            limit: int = 20
    ) -> list[Place]:
        response = await self._http_client.get(
            url="/search?",
            params={
                "sw": f"{latitude_min},{longitude_min}",
                "ne": f"{latitude_max},{longitude_max}",
                "categories": "19014",
                "sort": "RATING",
                "limit": limit
            }
        )
        if response.status_code != 200:
            return []
        raw_results = response.json()["results"]
        return list(map(self.json_to_schema, raw_results))

    @noself(cache)(ttl="3d")
    async def suggest_caterings(
            self,
            latitude: float,
            longitude: float,
            radius: int = 1000,
            limit: int = 20
    ) -> list[Place]:
        response = await self._http_client.get(
            url="/search?",
            params={
                "ll": f"{latitude},{longitude}",
                "radius": radius,
                "categories": "13065,13032",
                "sort": "RATING",
                "limit": limit
            }
        )
        if response.status_code != 200:
            return []
        raw_results = response.json()["results"]
        return list(map(self.json_to_schema, raw_results))

    @staticmethod
    def json_to_schema(data: dict[str, Any]) -> Place:
        return Place(
            id=data["fsq_id"],
            name=data["name"],
            description=data.get("description"),
            price=data.get("price"),
            latitude=data["geocodes"]["main"]["latitude"],
            longitude=data["geocodes"]["main"]["longitude"],
            address=data["location"]["formatted_address"],
            rating=data.get("rating")
        )

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aenter__(self) -> "FourSquareAPI":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
