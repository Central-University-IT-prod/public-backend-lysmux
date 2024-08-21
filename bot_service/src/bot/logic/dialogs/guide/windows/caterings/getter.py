from typing import Any

from aiogram_dialog import DialogManager

from resources_api import APIGateway
from travel_api import TravelApi


async def data_getter(
        api_gateway: APIGateway,
        travel_api: TravelApi,
        dialog_manager: DialogManager,
        **kwargs
) -> dict[str, Any]:
    from_loc_type: str = dialog_manager.dialog_data["from"]

    if from_loc_type == "current":
        latitude: float = dialog_manager.dialog_data["latitude"]
        longitude: float = dialog_manager.dialog_data["longitude"]
    else:
        location_id: str = dialog_manager.start_data["location_id"]
        travel_location = await travel_api.get_travel_location(location_id)
        latitude = travel_location.latitude
        longitude = travel_location.longitude

    caterings = await api_gateway.places_api.suggest_caterings(
        latitude=latitude,
        longitude=longitude,
    )

    return {
        "caterings": caterings
    }
