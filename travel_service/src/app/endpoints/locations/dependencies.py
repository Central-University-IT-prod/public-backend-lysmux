from typing import Annotated

from fastapi import Path, Depends

from app.dependencies import DBSessionDep
from core.database.repositories import LocationRepository
from core.schemas.location import LocationSchema
from core.services import LocationService
from .errors import LOCATION_NOT_FOUND


def get_location_service(
        db_session: DBSessionDep
) -> LocationService:
    repository = LocationRepository(db_session)
    service = LocationService(repository=repository)

    return service


LocationServiceDep = Annotated[LocationService, Depends(get_location_service)]


async def get_location(
        location_id: Annotated[str, Path()],
        location_service: LocationServiceDep
) -> LocationSchema:
    location = await location_service.get_by_id(location_id)
    if location is None:
        raise LOCATION_NOT_FOUND
    return location


LocationDep = Annotated[LocationSchema, Depends(get_location)]
