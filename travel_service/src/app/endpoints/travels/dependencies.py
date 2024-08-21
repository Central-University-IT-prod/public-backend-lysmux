from typing import Annotated

from fastapi import Path, Depends

from app.dependencies import DBSessionDep
from core.database.repositories import TravelRepository
from core.database.repositories.participant import ParticipantRepository
from core.schemas.travel import TravelSchema
from core.services import TravelService
from .errors import TRAVEL_NOT_FOUND


def get_travel_service(
        db_session: DBSessionDep
) -> TravelService:
    repository = TravelRepository(db_session)
    participant_repository = ParticipantRepository(db_session)
    service = TravelService(
        repository=repository,
        participant_repository=participant_repository
    )

    return service


TravelServiceDep = Annotated[TravelService, Depends(get_travel_service)]


async def get_travel(
        travel_id: Annotated[str, Path()],
        travel_service: TravelServiceDep
) -> TravelSchema:
    travel = await travel_service.get_by_id(travel_id)
    if travel is None:
        raise TRAVEL_NOT_FOUND
    return travel


TravelDep = Annotated[TravelSchema, Depends(get_travel)]
