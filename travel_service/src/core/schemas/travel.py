from pydantic import UUID4

from .base import BaseSchema
from .location import LocationSchema
from .note import NoteSchema
from .user import UserSchema


class TravelSchema(BaseSchema):
    id: UUID4
    owner: UserSchema
    name: str
    description: str
    locations: list[LocationSchema]
    notes: list[NoteSchema]
    participants: list[UserSchema]


class TravelCreateSchema(BaseSchema):
    owner_id: int
    name: str
    description: str


class TravelUpdateSchema(BaseSchema):
    name: str | None = None
    description: str | None = None
