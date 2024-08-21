from datetime import datetime

from pydantic import BaseModel


class SeatsGroup(BaseModel):
    min_price: float
    max_price: float
    type: str
    count: int
    class_name: str


class RzdTicket(BaseModel):
    train_number: str
    train_name: str
    from_station: str
    to_station: str
    departure_at: datetime
    arrival_at: datetime
    seats: list[SeatsGroup]


class CityCode(BaseModel):
    code: str
    bus_code: str
