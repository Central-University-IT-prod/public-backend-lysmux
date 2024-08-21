from datetime import date
from typing import Annotated

from fastapi import APIRouter, Query

from app.dependencies import RzdAPIDep
from app.errors import TRAIN_CITY_CODE_NOT_FOUND
from rzd_api.schemas import CityCode, RzdTicket

router = APIRouter(
    prefix="/tickets/train",
    tags=["Train tickets"]
)


@router.get(
    path="/city_code",
    response_model=CityCode
)
async def get_city_code(
        rzd_api: RzdAPIDep,
        city: Annotated[str, Query()],
) -> CityCode:
    city_code = await rzd_api.get_city_code(city)
    if city_code is None:
        raise TRAIN_CITY_CODE_NOT_FOUND

    return city_code


@router.get(
    path="",
    response_model=list[RzdTicket]
)
async def search_tickets(
        rzd_api: RzdAPIDep,
        from_station: Annotated[str, Query()],
        to_station: Annotated[str, Query()],
        departure_date: Annotated[date, Query()],
) -> list[RzdTicket]:
    tickets = await rzd_api.get_tickets(
        from_station=from_station,
        to_station=to_station,
        departure_date=departure_date
    )
    return tickets
