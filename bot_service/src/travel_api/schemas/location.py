from datetime import date

from pydantic import BaseModel


class TravelLocation(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float
    start_date: date
    end_date: date


class TravelLocationCreate(BaseModel):
    travel_id: str
    name: str
    latitude: float
    longitude: float
    start_date: date
    end_date: date


class TravelLocationUpdate(BaseModel):
    name: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    start_date: date | None = None
    end_date: date | None = None
