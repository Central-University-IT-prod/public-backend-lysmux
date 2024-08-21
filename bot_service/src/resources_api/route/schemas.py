from pydantic import BaseModel


class Location(BaseModel):
    display_name: str
    name: str
    latitude: float
    longitude: float
    osm_id: int
    bounding_box: list[float]
