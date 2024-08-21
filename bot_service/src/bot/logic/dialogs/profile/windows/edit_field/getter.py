from typing import Any

from aiogram.types import User

from travel_api import TravelApi


async def data_getter(
        travel_api: TravelApi,
        event_from_user: User,
        **kwargs
) -> dict[str, Any]:
    user = await travel_api.get_user(event_from_user.id)
    return {
        "user": user
    }
