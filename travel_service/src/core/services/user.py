from core.database.models import UserModel
from core.database.repositories import UserRepository
from core.schemas.user import (
    UserSchema,
    UserCreateSchema
)
from .base import BaseService


class UserService(
    BaseService[
        UserRepository,
        UserModel,
        UserSchema
    ]
):
    schema = UserSchema

    def __init__(
            self,
            repository: UserRepository
    ) -> None:
        super().__init__(repository)

    async def create(self, create_schema: UserCreateSchema) -> UserSchema:
        new_user = UserModel(
            id=create_schema.id,
            name=create_schema.name,
            age=create_schema.age,
            bio=create_schema.bio,
            latitude=create_schema.latitude,
            longitude=create_schema.longitude
        )
        await self.repository.create(new_user)
        return UserSchema.model_validate(new_user)
