from core.core_types import ID
from core.database.models import NoteModel
from core.database.repositories import NoteRepository
from core.schemas.note import NoteSchema, NoteCreateSchema
from .base import BaseService


class NoteService(
    BaseService[
        NoteRepository,
        NoteModel,
        NoteSchema
    ]
):
    schema = NoteSchema

    def __init__(
            self,
            repository: NoteRepository
    ) -> None:
        super().__init__(repository)

    async def create(
            self,
            create_schema: NoteCreateSchema
    ) -> NoteSchema:
        new_note = NoteModel(
            travel_id=create_schema.travel_id,
            owner_id=create_schema.owner_id,
            name=create_schema.name,
            content_type=create_schema.content_type,
            text=create_schema.text,
            file_id=create_schema.file_id,
            is_public=create_schema.is_public
        )
        await self.repository.create(new_note)
        return self.schema.model_validate(new_note)

    async def get_travel_notes(
            self,
            travel_id: ID
    ) -> list[NoteSchema]:
        models = await self.repository.get_travel_notes(travel_id)
        return self.models_to_schemas(models)
