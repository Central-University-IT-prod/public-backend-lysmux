from pydantic import UUID4

from .base import BaseSchema
from .user import UserSchema


class NoteSchema(BaseSchema):
    id: UUID4
    travel_id: UUID4
    name: str
    content_type: str
    text: str | None
    file_id: str | None
    is_public: bool
    owner: UserSchema


class NoteCreateSchema(BaseSchema):
    travel_id: UUID4
    owner_id: int
    name: str
    content_type: str
    text: str | None = None
    file_id: str | None = None
    is_public: bool


class NoteUpdateSchema(BaseSchema):
    name: str | None = None
    content_type: str | None = None
    text: str | None = None
    file_id: str | None = None
    is_public: bool | None = None
