from .base import BaseSchema


class UserSchema(BaseSchema):
    id: int
    name: str
    age: int
    bio: str
    latitude: float
    longitude: float


class UserCreateSchema(BaseSchema):
    id: int
    name: str
    age: int
    bio: str
    latitude: float
    longitude: float


class UserUpdateSchema(BaseSchema):
    age: int | None = None
    name: str | None = None
    bio: str | None = None
    latitude: float | None = None
    longitude: float | None = None
