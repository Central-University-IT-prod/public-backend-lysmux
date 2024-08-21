from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

from app.endpoints.travels.dependencies import TravelDep
from app.endpoints.users.dependencies import UserServiceDep, UserDep
from app.endpoints.users.errors import USER_NOT_FOUND
from core.schemas.responses import StatusResponse
from core.schemas.travel import (
    TravelSchema,
    TravelCreateSchema,
    TravelUpdateSchema
)
from .dependencies import TravelServiceDep
from .errors import (
    TRAVEL_NAME_EXISTS,
    FORBID_ADD_SELF_PARTICIPANT,
    PARTICIPANT_EXISTS
)

router = APIRouter(
    prefix="/travels"
)


@router.post(
    path="/create",
    response_model=TravelSchema
)
async def create_travel(
        create_schema: TravelCreateSchema,
        travel_service: TravelServiceDep,
        user_service: UserServiceDep
) -> TravelSchema:
    owner = await user_service.get_by_id(create_schema.owner_id)
    if owner is None:
        raise USER_NOT_FOUND

    try:
        travel = await travel_service.create(
            create_schema=create_schema
        )
    except IntegrityError:
        raise TRAVEL_NAME_EXISTS

    return travel


@router.delete(
    path="/{travel_id}",
    response_model=StatusResponse
)
async def delete_travel(
        travel: TravelDep,
        travel_service: TravelServiceDep
):
    await travel_service.delete(travel.id)
    return StatusResponse(status="ok")


@router.patch(
    path="/{travel_id}",
    response_model=TravelSchema
)
async def update_travel(
        travel: TravelDep,
        update_schema: TravelUpdateSchema,
        travel_service: TravelServiceDep
) -> TravelSchema:
    try:
        updated_travel = await travel_service.update(
            id_=travel.id,
            update_schema=update_schema
        )
    except IntegrityError:
        raise TRAVEL_NAME_EXISTS

    return updated_travel


@router.get(
    path="/{travel_id}",
    response_model=TravelSchema
)
async def get_travel(travel: TravelDep) -> TravelSchema:
    return travel


@router.get(
    path="/user/{user_id}",
    response_model=list[TravelSchema]
)
async def get_user_travels(
        user: UserDep,
        travel_service: TravelServiceDep
) -> list[TravelSchema]:
    travels = await travel_service.get_user_travels(user.id)
    return travels


@router.post(
    path="/{travel_id}/participant/{user_id}",
    response_model=StatusResponse
)
async def add_participant(
        user: UserDep,
        travel: TravelDep,
        travel_service: TravelServiceDep
) -> StatusResponse:
    if user.id == travel.owner.id:
        raise FORBID_ADD_SELF_PARTICIPANT

    try:
        await travel_service.add_participant(
            travel_id=travel.id,
            participant_id=user.id
        )
    except IntegrityError:
        raise PARTICIPANT_EXISTS

    return StatusResponse(status="ok")


@router.delete(
    path="/{travel_id}/participant/{user_id}",
    response_model=StatusResponse
)
async def remove_participant(
        user: UserDep,
        travel: TravelDep,
        travel_service: TravelServiceDep
) -> StatusResponse:
    await travel_service.remove_participant(
        travel_id=travel.id,
        participant_id=user.id
    )

    return StatusResponse(status="ok")
