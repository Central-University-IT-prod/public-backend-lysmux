from PIL import Image
from httpx import AsyncClient

from .models import MapMarker, MapLine
from .static_map import StaticMap

POINT_WIDTH = 10
POINT_COLOR = "RED"

LINE_WIDTH = 5
LINE_COLOR = "blue"


class RouteService:
    def __init__(self) -> None:
        self._http_client = AsyncClient()

    async def build_route(
            self,
            from_latitude: float,
            from_longitude: float,
            to_latitude: float,
            to_longitude: float,
    ) -> Image.Image | None:
        static_map = StaticMap()
        raw_route = await self._get_route(
            from_latitude=from_latitude,
            from_longitude=from_longitude,
            to_latitude=to_latitude,
            to_longitude=to_longitude
        )
        if raw_route["code"] == "NoRoute":
            return None

        points, steps = self._analyze_route(raw_route)
        for waypoint in points:
            static_map.add_marker(
                MapMarker(
                    coordinates=waypoint["location"],
                    width=POINT_WIDTH,
                    color=POINT_COLOR
                )
            )
        for step in steps:
            static_map.add_line(
                MapLine(
                    coordinates=step["geometry"]["coordinates"],
                    width=LINE_WIDTH,
                    color=LINE_COLOR
                )
            )
        map_obj = await static_map.render_map()
        await static_map.close()

        return map_obj

    async def _get_route(
            self,
            from_latitude: float,
            from_longitude: float,
            to_latitude: float,
            to_longitude: float,
    ) -> dict:
        response = await self._http_client.get(
            params={
                "overview": False,
                "geometries": "geojson",
                "steps": True
            },
            url=f"https://routing.openstreetmap.de/"
                f"routed-car/route/v1/driving/"
                f"{from_longitude},{from_latitude};"
                f"{to_longitude},{to_latitude}?"
        )
        return response.json()

    def _analyze_route(self, route: dict):
        points = route["waypoints"]
        steps = route["routes"][0]["legs"][0]["steps"]

        return points, steps

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aenter__(self) -> "RouteService":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
