from typing import Sequence, Any

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.core_types import ID
from core.database.models import BaseModel


class BaseRepository[M: BaseModel]:
    model_type: type[M]

    def __init__(
            self,
            session: AsyncSession
    ) -> None:
        self.session = session

    async def create(self, new_model: M) -> M:
        self.session.add(new_model)
        await self.session.flush()
        await self.session.refresh(new_model)

        return new_model

    async def batch_create(
            self,
            new_models: list[M]
    ) -> list[M]:
        self.session.add_all(new_models)
        await self.session.flush()

        return new_models

    async def delete(self, id_: ID) -> None:
        stmt = (
            delete(self.model_type)
            .where(self.model_type.id == id_)
        )
        await self.session.execute(stmt)

    async def update(
            self,
            id_: ID,
            data: dict[str, Any]
    ) -> M:
        model = await self.get_by_id(id_=id_)
        if model is None:
            raise ValueError(f"Could not find model with id={id_}")

        for key, value in data.items():
            if hasattr(model, key):
                setattr(model, key, value)

        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)

        return model

    async def get_by_id(self, id_: ID) -> M | None:
        stmt = select(self.model_type).where(self.model_type.id == id_)
        result = await self.session.execute(stmt)
        return result.scalar()

    async def get_all(
            self,
            limit: int | None = None,
            offset: int | None = None
    ) -> Sequence[M]:
        stmt = select(self.model_type).limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        return result.scalars().all()
