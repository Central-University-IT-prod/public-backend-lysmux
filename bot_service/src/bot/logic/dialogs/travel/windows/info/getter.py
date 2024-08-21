from typing import Any

from aiogram.types import User
from aiogram_dialog import DialogManager

from travel_api import TravelApi


async def data_getter(
        travel_api: TravelApi,
        dialog_manager: DialogManager,
        event_from_user: User,
        **kwargs
) -> dict[str, Any]:
    travel_id: str = dialog_manager.dialog_data["sel_travel_id"]
    travel = await travel_api.get_travel(travel_id)
    user_is_owner = travel.owner.id == event_from_user.id

    return {
        "travel": travel,
        "user_is_owner": user_is_owner
    }
