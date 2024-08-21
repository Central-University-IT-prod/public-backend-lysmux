from typing import Sequence

from sqlalchemy import select, or_

from core.core_types import ID
from core.database.models import TravelModel, ParticipantModel
from .base import BaseRepository


class TravelRepository(BaseRepository):
    model_type = TravelModel

    async def get_user_travels(self, user_id: ID) -> Sequence[TravelModel]:
        stmt = (
            select(self.model_type)
            .where(or_(
                self.model_type.owner_id == user_id,
                ParticipantModel.participant_id == user_id
            ))
            .outerjoin(
                ParticipantModel,
                onclause=ParticipantModel.travel_id == self.model_type.id
            )
            .order_by((self.model_type.owner_id == user_id).desc())
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
