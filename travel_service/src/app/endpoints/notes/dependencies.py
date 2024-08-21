from typing import Annotated

from fastapi import Path, Depends

from app.dependencies import DBSessionDep
from core.database.repositories import NoteRepository
from core.schemas.note import NoteSchema
from core.services import NoteService
from .errors import NOTE_NOT_FOUND


def get_note_service(
        db_session: DBSessionDep
) -> NoteService:
    repository = NoteRepository(db_session)
    service = NoteService(repository=repository)

    return service


NoteServiceDep = Annotated[NoteService, Depends(get_note_service)]


async def get_note(
        note_id: Annotated[str, Path()],
        note_service: NoteServiceDep
) -> NoteSchema:
    note = await note_service.get_by_id(note_id)
    if note is None:
        raise NOTE_NOT_FOUND
    return note


NoteDep = Annotated[NoteSchema, Depends(get_note)]
