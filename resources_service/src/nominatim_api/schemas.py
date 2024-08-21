from pydantic import BaseModel, Field


class Location(BaseModel):
    address_type: str = Field(validation_alias="addresstype")
    bounding_box: list[float] = Field(validation_alias="boundingbox")
    display_name: str
    latitude: float = Field(validation_alias="lat")
    longitude: float = Field(validation_alias="lon")
    name: str
    osm_id: int
