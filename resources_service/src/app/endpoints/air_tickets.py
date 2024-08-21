from datetime import date
from typing import Annotated

from fastapi import APIRouter, Query

from app.dependencies import KupiBiletAPIDep
from app.errors import AIRPORT_CODE_NOT_FOUND
from kupibilet_api.schemas import AirportCode, FlightTicket

router = APIRouter(
    prefix="/tickets/air",
    tags=["Train tickets"]
)


@router.get(
    path="/airport_code",
    response_model=AirportCode
)
async def get_airport_code(
        kupibilet_api: KupiBiletAPIDep,
        city: Annotated[str, Query()],
) -> AirportCode:
    airport_code = await kupibilet_api.get_airport_code(city)
    if airport_code is None:
        raise AIRPORT_CODE_NOT_FOUND

    return airport_code


@router.get(
    path="",
    response_model=list[FlightTicket]
)
async def search_tickets(
        kupibilet_api: KupiBiletAPIDep,
        from_airport: Annotated[str, Query()],
        to_airport: Annotated[str, Query()],
        departure_date: Annotated[date, Query()],
        persons: Annotated[int, Query()] = 1,
) -> list[FlightTicket]:
    tickets = await kupibilet_api.get_tickets(
        from_airport=from_airport,
        to_airport=to_airport,
        departure_date=departure_date,
        persons=persons
    )
    return tickets
