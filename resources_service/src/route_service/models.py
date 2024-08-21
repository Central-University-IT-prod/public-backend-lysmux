from dataclasses import dataclass

type COORDINATES = tuple[float, float]


@dataclass
class MapMarker:
    coordinates: COORDINATES
    color: str
    width: int


@dataclass
class MapLine:
    coordinates: list[COORDINATES]
    color: str
    width: int


@dataclass
class Tile:
    x: int
    y: int
    zoom: int


@dataclass
class Bounds:
    lat_min: float
    lon_min: float
    lat_max: float
    lon_max: float
