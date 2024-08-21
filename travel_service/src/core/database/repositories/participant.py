from typing import Sequence

from sqlalchemy import select, delete

from core.core_types import ID
from core.database.models import ParticipantModel
from .base import BaseRepository


class ParticipantRepository(BaseRepository):
    model_type = ParticipantModel

    async def get_travel_participants(
            self,
            travel_id: ID
    ) -> Sequence[ParticipantModel]:
        stmt = (
            select(self.model_type)
            .where(self.model_type.travel_id == travel_id)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def remove_participant(
            self,
            travel_id: ID,
            participant_id: ID
    ) -> None:
        stmt = (
            delete(self.model_type)
            .where(
                self.model_type.travel_id == travel_id,
                self.model_type.participant_id == participant_id
            )
        )
        await self.session.execute(stmt)
