from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .user import UserModel
    from .note import NoteModel
    from .location import LocationModel


class TravelModel(BaseModel):
    __tablename__ = "travels"

    name: Mapped[str]
    description: Mapped[str]
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade")
    )

    owner: Mapped["UserModel"] = relationship(
        back_populates="owned_travels",
        lazy="joined",
        uselist=False
    )
    locations: Mapped[list["LocationModel"]] = relationship(
        back_populates="travel",
        lazy="selectin",
        uselist=True,
        cascade="all, delete-orphan"
    )
    notes: Mapped[list["NoteModel"]] = relationship(
        back_populates="travel",
        lazy="selectin",
        uselist=True,
        cascade="all, delete-orphan"
    )
    participants: Mapped[list["UserModel"]] = relationship(
        back_populates="invited_travels",
        secondary="travel_participants",
        lazy="selectin",
        uselist=True
    )

    __table_args__ = (
        UniqueConstraint("name", "owner_id"),
    )
