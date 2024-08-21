from core.core_types import ID
from core.database.models import LocationModel
from core.database.repositories import LocationRepository
from core.schemas.location import (
    LocationSchema,
    LocationCreateSchema
)
from .base import BaseService


class LocationService(
    BaseService[
        LocationRepository,
        LocationModel,
        LocationSchema
    ]
):
    schema = LocationSchema

    def __init__(
            self,
            repository: LocationRepository
    ) -> None:
        super().__init__(repository)

    async def create(
            self,
            create_schema: LocationCreateSchema
    ) -> LocationSchema:
        new_location = LocationModel(
            travel_id=create_schema.travel_id,
            name=create_schema.name,
            latitude=create_schema.latitude,
            longitude=create_schema.longitude,
            start_date=create_schema.start_date,
            end_date=create_schema.end_date,
        )
        await self.repository.create(new_location)
        return self.schema.model_validate(new_location)

    async def get_travel_locations(
            self,
            travel_id: ID
    ) -> list[LocationSchema]:
        models = await self.repository.get_travel_locations(travel_id)
        return self.models_to_schemas(models)
