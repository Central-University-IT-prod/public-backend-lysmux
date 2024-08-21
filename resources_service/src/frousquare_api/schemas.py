from pydantic import BaseModel


class Place(BaseModel):
    id: str
    name: str
    description: str | None = None
    latitude: float
    longitude: float
    address: str
    rating: float | None = None
    price: int | None = None
