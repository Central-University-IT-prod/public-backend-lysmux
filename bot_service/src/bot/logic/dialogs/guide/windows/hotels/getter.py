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
    location_id: str = dialog_manager.start_data["location_id"]
    travel_location = await travel_api.get_travel_location(location_id)
    location = await api_gateway.location_api.from_coordinates(
        latitude=travel_location.latitude,
        longitude=travel_location.longitude,
        city=True
    )
    hotels = await api_gateway.places_api.suggest_hotels(
        latitude_min=location.bounding_box[0],
        latitude_max=location.bounding_box[1],
        longitude_min=location.bounding_box[2],
        longitude_max=location.bounding_box[3]
    )

    return {
        "hotels": hotels
    }
