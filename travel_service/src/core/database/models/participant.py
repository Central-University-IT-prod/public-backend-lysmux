from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .base import BaseModel


class ParticipantModel(BaseModel):
    __tablename__ = "travel_participants"

    travel_id: Mapped[str] = mapped_column(
        ForeignKey("travels.id", ondelete="cascade")
    )
    participant_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="cascade")
    )

    __table_args__ = (
        UniqueConstraint("travel_id", "participant_id"),
    )
