from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError

from core.schemas.user import (
    UserCreateSchema,
    UserSchema,
    UserUpdateSchema
)
from .dependencies import UserDep, UserServiceDep
from .errors import USER_EXISTS

router = APIRouter(
    prefix="/users"
)


@router.post(
    path="/create",
    response_model=UserSchema
)
async def create_user(
        create_schema: UserCreateSchema,
        user_service: UserServiceDep
) -> UserSchema:
    try:
        new_user = await user_service.create(create_schema)
    except IntegrityError:
        raise USER_EXISTS
    return new_user


@router.get(
    path="/{user_id}",
    response_model=UserSchema
)
async def get_user(
        user: UserDep
) -> UserSchema:
    return user


@router.patch(
    path="/{user_id}",
    response_model=UserSchema
)
async def update_user(
        user: UserDep,
        update_schema: UserUpdateSchema,
        user_service: UserServiceDep
) -> UserSchema:
    updated_user = await user_service.update(
        id_=user.id,
        update_schema=update_schema
    )
    return updated_user
