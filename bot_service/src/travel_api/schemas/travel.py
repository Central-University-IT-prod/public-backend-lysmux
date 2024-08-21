from pydantic import BaseModel, Field

from .user import User


class Travel(BaseModel):
    id: str
    owner: User
    name: str
    description: str
    participants: list[User] = Field(default_factory=list)


class TravelCreate(BaseModel):
    owner_id: int
    name: str
    description: str


class TravelUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
