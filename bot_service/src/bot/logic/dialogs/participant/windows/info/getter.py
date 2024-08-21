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
    travel_id: str = dialog_manager.start_data["travel_id"]
    participant_id: int = dialog_manager.dialog_data["sel_participant_id"]
    participant = await travel_api.get_user(participant_id)
    travel = await travel_api.get_travel(travel_id)
    user_is_owner = travel.owner.id == event_from_user.id

    return {
        "participant": participant,
        "participant_id": participant.id,
        "owner_id": travel.owner.id,
        "user_is_owner": user_is_owner
    }
