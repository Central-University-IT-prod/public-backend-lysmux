from typing import Sequence

from sqlalchemy import select

from core.core_types import ID
from core.database.models import LocationModel
from .base import BaseRepository


class LocationRepository(BaseRepository):
    model_type = LocationModel

    async def get_travel_locations(
            self,
            travel_id: ID
    ) -> Sequence[LocationModel]:
        stmt = (
            select(self.model_type)
            .where(self.model_type.travel_id == travel_id)
            .order_by(self.model_type.start_date.asc())
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
