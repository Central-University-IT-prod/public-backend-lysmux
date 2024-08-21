from io import BytesIO

from resources_api.base_api import ApiClient


class RouteAPI(ApiClient):
    async def build_route(
            self,
            from_latitude: float,
            from_longitude: float,
            to_latitude: float,
            to_longitude: float,
    ) -> BytesIO | None:
        response = await self._http_client.get(
            url="/route?",
            params={
                "from_latitude": from_latitude,
                "from_longitude": from_longitude,
                "to_latitude": to_latitude,
                "to_longitude": to_longitude
            }
        )
        if response.status_code != 200:
            return None
        return BytesIO(response.content)
