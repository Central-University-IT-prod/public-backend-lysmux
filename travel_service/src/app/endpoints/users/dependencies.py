from typing import Annotated

from fastapi import Path, Depends

from app.dependencies import DBSessionDep
from core.database.repositories import UserRepository
from core.schemas.user import UserSchema
from core.services import UserService
from .errors import USER_NOT_FOUND


def get_user_service(
        db_session: DBSessionDep
) -> UserService:
    repository = UserRepository(db_session)
    service = UserService(repository=repository)

    return service


UserServiceDep = Annotated[UserService, Depends(get_user_service)]


async def get_user(
        user_id: Annotated[int, Path()],
        user_service: UserServiceDep
) -> UserSchema:
    user = await user_service.get_by_id(user_id)
    if user is None:
        raise USER_NOT_FOUND
    return user


UserDep = Annotated[UserSchema, Depends(get_user)]
