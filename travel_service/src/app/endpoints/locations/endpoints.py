from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

from app.endpoints.travels.dependencies import TravelDep, TravelServiceDep
from app.endpoints.travels.errors import TRAVEL_NOT_FOUND
from core.schemas.location import (
    LocationSchema,
    LocationCreateSchema,
    LocationUpdateSchema
)
from core.schemas.responses import StatusResponse
from .dependencies import LocationDep, LocationServiceDep
from .errors import LOCATION_NAME_EXISTS

router = APIRouter(
    prefix="/locations"
)


@router.post(
    path="/add",
    response_model=LocationSchema
)
async def add_location(
        create_schema: LocationCreateSchema,
        location_service: LocationServiceDep,
        travel_service: TravelServiceDep
) -> LocationSchema:
    travel = await travel_service.get_by_id(create_schema.travel_id)
    if travel is None:
        raise TRAVEL_NOT_FOUND

    try:
        location = await location_service.create(
            create_schema=create_schema
        )
    except IntegrityError:
        raise LOCATION_NAME_EXISTS

    return location


@router.delete(
    path="/{location_id}",
    response_model=StatusResponse
)
async def delete_location(
        location: LocationDep,
        location_service: LocationServiceDep
) -> StatusResponse:
    await location_service.delete(location.id)
    return StatusResponse(status="ok")


@router.patch(
    path="/{location_id}",
    response_model=LocationSchema
)
async def update_location(
        location: LocationDep,
        update_schema: LocationUpdateSchema,
        location_service: LocationServiceDep
) -> LocationSchema:
    try:
        updated_location = await location_service.update(
            id_=location.id,
            update_schema=update_schema
        )
    except IntegrityError:
        raise LOCATION_NAME_EXISTS

    return updated_location


@router.get(
    path="/travel/{travel_id}",
    response_model=list[LocationSchema]
)
async def get_locations(
        travel: TravelDep,
        location_service: LocationServiceDep
) -> list[LocationSchema]:
    locations = await location_service.get_travel_locations(travel.id)
    return locations


@router.get(
    path="/{location_id}",
    response_model=LocationSchema
)
async def get_location(location: LocationDep) -> LocationSchema:
    return location
