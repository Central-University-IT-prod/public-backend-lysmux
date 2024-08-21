from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

from app.endpoints.travels.dependencies import TravelDep, TravelServiceDep
from app.endpoints.travels.errors import TRAVEL_NOT_FOUND
from app.endpoints.users.dependencies import UserServiceDep
from app.endpoints.users.errors import USER_NOT_FOUND
from core.schemas.note import (
    NoteSchema,
    NoteCreateSchema,
    NoteUpdateSchema
)
from core.schemas.responses import StatusResponse
from .dependencies import NoteDep, NoteServiceDep
from .errors import NOTE_NAME_EXISTS

router = APIRouter(
    prefix="/notes"
)


@router.post(
    path="/add",
    response_model=NoteSchema
)
async def add_note(
        create_schema: NoteCreateSchema,
        note_service: NoteServiceDep,
        travel_service: TravelServiceDep,
        user_service: UserServiceDep
) -> NoteSchema:
    user = await user_service.get_by_id(create_schema.owner_id)
    if user is None:
        raise USER_NOT_FOUND

    travel = await travel_service.get_by_id(create_schema.travel_id)
    if travel is None:
        raise TRAVEL_NOT_FOUND

    try:
        note = await note_service.create(
            create_schema=create_schema
        )
    except IntegrityError:
        raise NOTE_NAME_EXISTS

    return note


@router.delete(
    path="/{note_id}",
    response_model=StatusResponse
)
async def delete_note(
        note: NoteDep,
        note_service: NoteServiceDep
) -> StatusResponse:
    await note_service.delete(note.id)
    return StatusResponse(status="ok")


@router.patch(
    path="/{note_id}",
    response_model=NoteSchema
)
async def update_note(
        note: NoteDep,
        update_schema: NoteUpdateSchema,
        note_service: NoteServiceDep
) -> NoteSchema:
    try:
        updated_note = await note_service.update(
            id_=note.id,
            update_schema=update_schema
        )
    except IntegrityError:
        raise NOTE_NAME_EXISTS

    return updated_note


@router.get(
    path="/travel/{travel_id}",
    response_model=list[NoteSchema]
)
async def get_notes(
        travel: TravelDep,
        note_service: NoteServiceDep
) -> list[NoteSchema]:
    notes = await note_service.get_travel_notes(travel.id)
    return notes


@router.get(
    path="/{note_id}",
    response_model=NoteSchema
)
async def get_note(note: NoteDep) -> NoteSchema:
    return note
