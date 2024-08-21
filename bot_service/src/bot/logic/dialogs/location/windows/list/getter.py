from typing import Any

from aiogram_dialog import DialogManager

from travel_api import TravelApi


async def data_getter(
        travel_api: TravelApi,
        dialog_manager: DialogManager,
        **kwargs
) -> dict[str, Any]:
    travel_id: str = dialog_manager.start_data["travel_id"]
    locations = await travel_api.get_travel_locations(travel_id)

    return {
        "locations": locations
    }
