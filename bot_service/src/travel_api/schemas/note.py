from pydantic import BaseModel

from .user import User


class Note(BaseModel):
    id: str
    owner: User
    name: str
    file_id: str | None = None
    content_type: str | None = None
    text: str | None
    is_public: bool


class NoteCreate(BaseModel):
    travel_id: str
    owner_id: int
    name: str
    content_type: str
    file_id: str | None = None
    text: str | None
    is_public: bool


class NoteUpdate(BaseModel):
    name: str | None = None
    content_type: str | None = None
    file_id: str | None = None
    text: str | None = None
    is_public: bool | None = None
