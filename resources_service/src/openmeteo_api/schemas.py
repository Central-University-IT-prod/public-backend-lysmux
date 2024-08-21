from pydantic import BaseModel
from datetime import date


class Forecast(BaseModel):
    date: date
    temperature_min: float
    temperature_max: float
    temperature_apparent_min: float
    temperature_apparent_max: float
    precipitation_probability: int
    wind_speed: float
    wind_direction: int
