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
    forecasts = await api_gateway.forecast_api.forecast(
        latitude=travel_location.latitude,
        longitude=travel_location.longitude,
        start_date=travel_location.start_date,
        end_date=travel_location.end_date
    )

    return {
        "forecasts": forecasts
    }
