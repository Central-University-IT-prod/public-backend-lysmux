from datetime import date

from pydantic import UUID4

from .base import BaseSchema


class LocationSchema(BaseSchema):
    id: UUID4
    name: str
    latitude: float
    longitude: float
    start_date: date
    end_date: date


class LocationCreateSchema(BaseSchema):
    travel_id: UUID4
    name: str
    latitude: float
    longitude: float
    start_date: date
    end_date: date


class LocationUpdateSchema(BaseSchema):
    name: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    start_date: date | None = None
    end_date: date | None = None
