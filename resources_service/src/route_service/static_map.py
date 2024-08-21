import asyncio
import math
from io import BytesIO

from PIL import Image
from PIL.ImageDraw import ImageDraw
from httpx import AsyncClient

from .models import MapMarker, MapLine, Bounds, Tile
from .utils import lat_to_y, lon_to_x

TILE_SERVER_TEMPLATE = "https://tile.openstreetmap.org/{zoom}/{x}/{y}.png"
TILE_SIZE = 256

DEFAULT_MAP_WIDTH = 1920
DEFAULT_MAP_HEIGHT = 1080

DEFAULT_BACKGROUND_COLOR = "white"


class StaticMap:
    def __init__(
            self,
            map_width: int = DEFAULT_MAP_WIDTH,
            map_height: int = DEFAULT_MAP_HEIGHT,
            background_color: str = DEFAULT_BACKGROUND_COLOR
    ) -> None:
        self._http_client = AsyncClient()

        self.map_width = map_width
        self.map_height = map_height

        self.background_color = background_color

        self.markers: list[MapMarker] = []
        self.lines: list[MapLine] = []

    def add_line(self, line: MapLine) -> None:
        self.lines.append(line)

    def add_marker(self, marker: MapMarker) -> None:
        self.markers.append(marker)

    async def render_map(self) -> Image.Image:
        image = Image.new(
            mode="RGB",
            size=(self.map_width, self.map_height),
            color=self.background_color
        )
        map_img = await self._render_map()
        features_img = await self._render_features()

        image.paste(map_img, mask=map_img)
        image.paste(features_img, mask=features_img)

        return image

    async def _render_map(self) -> Image.Image:
        image = Image.new(
            mode="RGBA",
            size=(self.map_width, self.map_height),
            color=(0, 0, 0, 0)
        )
        tiles = self._determine_tiles()
        tasks = [
            self._download_tile(tile)
            for tile in tiles
        ]
        results = await asyncio.gather(*tasks)

        for tile, tile_img in zip(tiles, results):
            image.paste(
                im=tile_img,
                box=(
                    self._x_to_px(tile.x),
                    self._y_to_px(tile.y),
                    self._x_to_px(tile.x + 1),
                    self._y_to_px(tile.y + 1),
                )
            )

        return image

    async def _render_features(self) -> Image.Image:
        zoom = self._calculate_zoom()
        image = Image.new(
            mode="RGBA",
            size=(self.map_width, self.map_height),
            color=(0, 0, 0, 0)
        )
        draw = ImageDraw(image)

        for line in self.lines:
            points = [(
                self._x_to_px(lon_to_x(coord[0], zoom)),
                self._y_to_px(lat_to_y(coord[1], zoom)),
            ) for coord in line.coordinates]

            draw.line(points, fill=line.color, width=line.width)

        for marker in self.markers:
            point = (
                self._x_to_px(lon_to_x(marker.coordinates[0], zoom)),
                self._y_to_px(lat_to_y(marker.coordinates[1], zoom))
            )
            draw.ellipse((
                point[0] - marker.width,
                point[1] - marker.width,
                point[0] + marker.width,
                point[1] + marker.width
            ), fill=marker.color)

        return image

    def _determine_tiles(self) -> list[Tile]:
        zoom = self._calculate_zoom()
        center_x, center_y = self._calculate_center()
        x_min = int(math.floor(center_x - (0.5 * self.map_width / TILE_SIZE)))
        y_min = int(math.floor(center_y - (0.5 * self.map_height / TILE_SIZE)))
        x_max = int(math.ceil(center_x + (0.5 * self.map_width / TILE_SIZE)))
        y_max = int(math.ceil(center_y + (0.5 * self.map_height / TILE_SIZE)))

        return [
            Tile(x=x, y=y, zoom=zoom)
            for x in range(x_min, x_max)
            for y in range(y_min, y_max)
        ]

    def _determine_bounds(self) -> Bounds:
        return Bounds(
            lat_min=min(marker.coordinates[1] for marker in self.markers),
            lon_min=min(marker.coordinates[0] for marker in self.markers),
            lat_max=max(marker.coordinates[1] for marker in self.markers),
            lon_max=max(marker.coordinates[0] for marker in self.markers),
        )

    def _calculate_zoom(self) -> int:
        border = self._determine_bounds()
        zoom_lon = math.log(
            360.0 / 256.0 * (self.map_width - 2) /
            ((border.lat_max - border.lat_min) or 1)
        ) / math.log(2)
        zoom_lat = math.log(
            180.0 / 256.0 * (self.map_height - 2) /
            ((border.lat_max - border.lat_min) or 1)
        ) / math.log(2)

        return int(min(zoom_lon, zoom_lat))

    def _calculate_center(self) -> tuple[float, float]:
        border = self._determine_bounds()
        zoom = self._calculate_zoom()
        lon_center = (border.lon_max + border.lon_min) / 2
        lat_center = (border.lat_max + border.lat_min) / 2
        center_x = lon_to_x(lon_center, zoom)
        center_y = lat_to_y(lat_center, zoom)

        return center_x, center_y

    def _x_to_px(self, x):
        center = self._calculate_center()
        px = (x - center[0]) * TILE_SIZE + self.map_width / 2
        return int(round(px))

    def _y_to_px(self, y):
        center = self._calculate_center()
        px = (y - center[1]) * TILE_SIZE + self.map_height / 2
        return int(round(px))

    async def _download_tile(self, tile: Tile) -> Image.Image:
        response = await self._http_client.get(
            url=TILE_SERVER_TEMPLATE.format(
                x=tile.x,
                y=tile.y,
                zoom=tile.zoom
            )
        )
        image = Image.open(BytesIO(response.content)).convert("RGBA")
        return image

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aenter__(self) -> "StaticMap":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
