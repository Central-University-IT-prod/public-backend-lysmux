from typing import Annotated

from fastapi import APIRouter, Query

from app.dependencies import NominatimAPIDep
from app.errors import LOCATION_NOT_FOUND
from nominatim_api.schemas import Location

router = APIRouter(
    prefix="/location",
    tags=["Location"]
)


@router.get(
    path="/search",
    response_model=Location
)
async def search(
        nominatim_api: NominatimAPIDep,
        query: Annotated[str, Query()],
        city: Annotated[bool, Query()] = False,
) -> Location:
    location = await nominatim_api.search(
        query=query,
        city=city
    )

    if location is None:
        raise LOCATION_NOT_FOUND

    return location


@router.get(
    path="/suggest",
    response_model=list[Location]
)
async def suggest(
        nominatim_api: NominatimAPIDep,
        query: Annotated[str, Query()],
        city: Annotated[bool, Query()] = False,
) -> list[Location]:
    location = await nominatim_api.suggest(
        query=query,
        city=city
    )

    return location


@router.get(
    path="/from_coordinates",
    response_model=Location
)
async def from_coordinates(
        nominatim_api: NominatimAPIDep,
        latitude: Annotated[float, Query(
            ge=-90,
            le=90
        )],
        longitude: Annotated[float, Query(
            ge=-180,
            le=180
        )],
        city: Annotated[bool, Query()] = False,
) -> Location:
    location = await nominatim_api.from_coordinates(
        latitude=latitude,
        longitude=longitude,
        city=city
    )

    if location is None:
        raise LOCATION_NOT_FOUND

    return location
