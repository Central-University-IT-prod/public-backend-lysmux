import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .user import UserModel
    from .travel import TravelModel


class NoteModel(BaseModel):
    __tablename__ = "notes"

    name: Mapped[str]
    content_type: Mapped[str]
    text: Mapped[str | None]
    file_id: Mapped[str | None]
    is_public: Mapped[bool]

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade")
    )
    travel_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("travels.id", ondelete="cascade")
    )

    owner: Mapped["UserModel"] = relationship(
        back_populates="owned_notes",
        lazy="joined",
        uselist=False
    )
    travel: Mapped["TravelModel"] = relationship(
        back_populates="notes",
        lazy="joined",
        uselist=False
    )

    __table_args__ = (
        UniqueConstraint("name", "travel_id"),
    )
