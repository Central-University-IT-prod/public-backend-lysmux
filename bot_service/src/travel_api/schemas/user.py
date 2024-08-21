from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int
    bio: str
    latitude: float
    longitude: float


class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    bio: str | None = None
    latitude: float | None = None
    longitude: float | None = None
