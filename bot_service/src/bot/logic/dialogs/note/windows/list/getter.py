from typing import Any

from aiogram.types import User
from aiogram_dialog import DialogManager
from travel_api.api import TravelApi


async def data_getter(
        travel_api: TravelApi,
        dialog_manager: DialogManager,
        event_from_user: User,
        **kwargs
) -> dict[str, Any]:
    travel_id: str = dialog_manager.start_data["travel_id"]
    notes = await travel_api.get_notes(travel_id)
    filtered_notes = list(filter(
        lambda note: note.owner.id == event_from_user.id, notes
    ))

    return {
        "notes": filtered_notes
    }
