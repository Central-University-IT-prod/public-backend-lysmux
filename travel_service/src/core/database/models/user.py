from typing import TYPE_CHECKING

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .travel import TravelModel
    from .note import NoteModel


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(  # type: ignore[reportIncompatibleVariableOverride] # noqa
        BigInteger,
        primary_key=True,
        autoincrement=False
    )

    name: Mapped[str]
    age: Mapped[int]
    bio: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]

    owned_travels: Mapped[list["TravelModel"]] = relationship(
        back_populates="owner",
        lazy="selectin",
        uselist=True
    )
    invited_travels: Mapped[list["TravelModel"]] = relationship(
        back_populates="participants",
        secondary="travel_participants",
        lazy="selectin",
        uselist=True
    )
    owned_notes: Mapped[list["NoteModel"]] = relationship(
        back_populates="owner",
        lazy="selectin",
        uselist=True
    )
