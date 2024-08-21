from abc import ABC
from typing import Sequence

from pydantic import TypeAdapter

from core.core_types import ID
from core.database.models import BaseModel
from core.database.repositories import BaseRepository
from core.schemas.base import BaseSchema


class BaseService[R: BaseRepository,
                  M: BaseModel,
                  S: BaseSchema](ABC):
    schema: type[S]

    def __init__(self, repository: R) -> None:
        self.repository = repository

    async def update(self, id_: ID, update_schema: BaseSchema) -> S:
        update_data = update_schema.model_dump(exclude_none=True)
        updated_user = await self.repository.update(
            id_=id_,
            data=update_data
        )
        return self.schema.model_validate(updated_user)

    async def delete(self, id_: ID) -> None:
        await self.repository.delete(id_=id_)

    async def get_all(
            self,
            limit: int = 1000,
            offset: int = 0
    ) -> list[S]:
        models = await self.repository.get_all(
            limit=limit,
            offset=offset
        )
        adapter = TypeAdapter(type=list[S])
        return adapter.validate_python(models)

    async def get_by_id(self, id_: ID) -> S | None:
        model = await self.repository.get_by_id(id_=id_)
        return self.schema_or_none(model)

    def schema_or_none(
            self,
            model: M | None
    ) -> S | None:
        if model is None:
            return None

        return self.schema.model_validate(model)

    def models_to_schemas(self, models: Sequence[M]) -> list[S]:
        adapter = TypeAdapter(type=list[self.schema])
        return adapter.validate_python(models)
