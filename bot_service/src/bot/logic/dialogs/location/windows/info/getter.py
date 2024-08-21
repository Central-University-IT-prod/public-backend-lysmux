from typing import Any

from aiogram.types import User
from aiogram_dialog import DialogManager

from resources_api import APIGateway
from travel_api import TravelApi


async def data_getter(
        travel_api: TravelApi,
        api_gateway: APIGateway,
        dialog_manager: DialogManager,
        event_from_user: User,
        **kwargs
) -> dict[str, Any]:
    travel_id: str = dialog_manager.start_data["travel_id"]
    location_id: str = dialog_manager.dialog_data["sel_location_id"]
    travel_location = await travel_api.get_travel_location(location_id)
    location = await api_gateway.location_api.from_coordinates(
        latitude=travel_location.latitude,
        longitude=travel_location.longitude,
        city=True
    )
    travel = await travel_api.get_travel(travel_id)
    user_is_owner = travel.owner.id == event_from_user.id

    return {
        "travel_location": travel_location,
        "location": location,
        "user_is_owner": user_is_owner
    }
