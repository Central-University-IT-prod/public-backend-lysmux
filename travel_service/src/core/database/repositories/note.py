from typing import Sequence

from sqlalchemy import select

from core.core_types import ID
from core.database.models import NoteModel
from .base import BaseRepository


class NoteRepository(BaseRepository):
    model_type = NoteModel

    async def get_travel_notes(self, travel_id: ID) -> Sequence[NoteModel]:
        stmt = (
            select(self.model_type)
            .where(self.model_type.travel_id == travel_id)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
