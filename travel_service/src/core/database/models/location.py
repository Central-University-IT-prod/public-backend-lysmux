from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import BaseModel

if TYPE_CHECKING:
    from .travel import TravelModel


class LocationModel(BaseModel):
    __tablename__ = "travel_locations"

    travel_id: Mapped[str] = mapped_column(
        ForeignKey("travels.id", ondelete="cascade")
    )
    name: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    start_date: Mapped[date]
    end_date: Mapped[date]

    travel: Mapped["TravelModel"] = relationship(
        back_populates="locations",
        lazy="joined",
        uselist=False
    )

    __table_args__ = (
        UniqueConstraint("travel_id", "name"),
    )
