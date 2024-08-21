from datetime import datetime

from pydantic import BaseModel, Field


class SeatsGroup(BaseModel):
    min_price: float = Field(validation_alias="MinPrice")
    max_price: float = Field(validation_alias="MaxPrice")
    type: str = Field(validation_alias="CarType")
    count: int = Field(validation_alias="PlaceQuantity")
    class_name: str = Field(validation_alias="ServiceClassName")


class RzdTicket(BaseModel):
    train_number: str = Field(validation_alias="TrainNumber")
    train_name: str = Field(validation_alias="TrainName")
    from_station: str = Field(validation_alias="OriginStationName")
    to_station: str = Field(validation_alias="DestinationStationName")
    departure_at: datetime = Field(validation_alias="DepartureDateTime")
    arrival_at: datetime = Field(validation_alias="ArrivalDateTime")
    seats: list[SeatsGroup] = Field(validation_alias="CarGroups")


class CityCode(BaseModel):
    code: str = Field(validation_alias="expressCode")
    bus_code: str = Field(validation_alias="busCode")
