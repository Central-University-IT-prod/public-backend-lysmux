from cashews import cache, noself
from httpx import AsyncClient
from pydantic import TypeAdapter

from nominatim_api.schemas import Location


class NominatimAPI:
    BASE_URL = "https://nominatim.openstreetmap.org"
    USER_AGENT = "Location service/tg travel bot"

    def __init__(self) -> None:
        self._http_client = AsyncClient(
            base_url=self.BASE_URL,
            follow_redirects=True,
            params={
                "format": "jsonv2",
                "addressdetails": 1,
            },
            headers={
                "Accept-Language": "ru-RU",
                "User-Agent": self.USER_AGENT
            }
        )

    @noself(cache)(ttl="7d")
    async def suggest(
            self,
            query: str,
            city: bool = False
    ) -> list[Location]:
        request = await self._http_client.get(
            url="search?",
            params={
                "q": query,
                "featureType": "city" if city else None
            }
        )
        ta = TypeAdapter(type=list[Location])
        return ta.validate_python(request.json())

    @noself(cache)(ttl="7d")
    async def search(
            self,
            query: str,
            city: bool = False
    ) -> Location | None:
        request = await self._http_client.get(
            url="search?",
            params={
                "q": query,
                "limit": 1,
                "featureType": "city" if city else None
            }
        )
        json = request.json()
        if not json:
            return None

        return Location.model_validate(json[0])

    @noself(cache)(ttl="7d")
    async def from_coordinates(
            self,
            latitude: float,
            longitude: float,
            city: bool = False
    ) -> Location | None:
        request = await self._http_client.get(
            url="reverse?",
            params={
                "lat": latitude,
                "lon": longitude,
                "zoom": 10 if city else 16
            }
        )
        json = request.json()
        if not json:
            return None
        if "error" in json:
            return None

        return Location.model_validate(json)

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aenter__(self) -> "NominatimAPI":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
