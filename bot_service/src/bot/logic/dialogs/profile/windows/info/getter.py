from typing import Any

from aiogram.types import User

from resources_api import APIGateway
from travel_api import TravelApi


async def data_getter(
        travel_api: TravelApi,
        api_gateway: APIGateway,
        event_from_user: User,
        **kwargs
) -> dict[str, Any]:
    user = await travel_api.get_user(event_from_user.id)

    if user:
        location = await api_gateway.location_api.from_coordinates(
            latitude=user.latitude,
            longitude=user.longitude
        )

        return {
            "user": user,
            "location": location
        }
    return {
        "user": None
    }
