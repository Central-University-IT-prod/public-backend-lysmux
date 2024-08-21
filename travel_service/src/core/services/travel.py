from core.core_types import ID
from core.database.models import TravelModel, ParticipantModel
from core.database.repositories import TravelRepository
from core.database.repositories.participant import ParticipantRepository
from core.schemas.travel import (
    TravelSchema,
    TravelCreateSchema
)
from .base import BaseService


class TravelService(
    BaseService[
        TravelRepository,
        TravelModel,
        TravelSchema
    ]
):
    schema = TravelSchema

    def __init__(
            self,
            repository: TravelRepository,
            participant_repository: ParticipantRepository

    ) -> None:
        super().__init__(repository)

        self.participant_repository = participant_repository

    async def create(
            self,
            create_schema: TravelCreateSchema
    ) -> TravelSchema:
        new_travel = TravelModel(
            owner_id=create_schema.owner_id,
            name=create_schema.name,
            description=create_schema.description
        )
        await self.repository.create(new_travel)
        return self.schema.model_validate(new_travel)

    async def get_user_travels(self, user_id: ID) -> list[TravelSchema]:
        models = await self.repository.get_user_travels(user_id=user_id)
        return self.models_to_schemas(models)

    async def add_participant(
            self,
            travel_id: ID,
            participant_id: ID
    ) -> None:
        participant_model = ParticipantModel(
            travel_id=travel_id,
            participant_id=participant_id,
        )
        await self.participant_repository.create(participant_model)

    async def remove_participant(
            self,
            travel_id: ID,
            participant_id: ID
    ) -> None:
        await self.participant_repository.remove_participant(
            travel_id=travel_id,
            participant_id=participant_id,
        )
