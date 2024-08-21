from datetime import datetime

from pydantic import BaseModel


class FlightSegment(BaseModel):
    flight_number: str
    company: str
    aircraft: str

    departure_airport_code: str
    departure_airport_name: str
    departure_city_name: str

    arrival_airport_code: str
    arrival_airport_name: str
    arrival_city_name: str

    departure_at: datetime
    arrival_at: datetime


class FlightTicket(BaseModel):
    segments: list[FlightSegment]
    price: int
    buy_link: str


class AirportCode(BaseModel):
    code: str
