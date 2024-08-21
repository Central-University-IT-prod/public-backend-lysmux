from typing import Any

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from resources_api import APIGateway
from travel_api import TravelApi


async def data_getter(
        api_gateway: APIGateway,
        travel_api: TravelApi,
        dialog_manager: DialogManager,
        **kwargs
) -> dict[str, Any]:
    from_loc_type: str = dialog_manager.dialog_data["from"]

    location_id: str = dialog_manager.start_data["location_id"]
    to_travel_location = await travel_api.get_travel_location(location_id)

    if from_loc_type == "current":
        latitude: float = dialog_manager.dialog_data["latitude"]
        longitude: float = dialog_manager.dialog_data["longitude"]
        from_location = await api_gateway.location_api.from_coordinates(
            latitude=latitude,
            longitude=longitude,
            city=True
        )
    else:
        travel_id: str = dialog_manager.start_data["travel_id"]
        travel_locations = await travel_api.get_travel_locations(travel_id)
        cur_travel_loc_idx = travel_locations.index(to_travel_location)
        cur_travel_loc_idx = cur_travel_loc_idx if cur_travel_loc_idx > 0 else 1
        prev_travel_loc = travel_locations[cur_travel_loc_idx - 1]

        from_location = await api_gateway.location_api.from_coordinates(
            latitude=prev_travel_loc.latitude,
            longitude=prev_travel_loc.longitude,
            city=True
        )

    to_location = await api_gateway.location_api.from_coordinates(
        latitude=to_travel_location.latitude,
        longitude=to_travel_location.longitude,
        city=True
    )

    route = await api_gateway.route_api.build_route(
        from_latitude=from_location.latitude,
        from_longitude=from_location.longitude,
        to_latitude=to_location.latitude,
        to_longitude=to_location.longitude
    )
    if route is not None:
        route_img = MediaAttachment(
            type=ContentType.PHOTO,
            url=route.getvalue()
        )

        return {
            "route_img": route_img
        }
    return {
        "route_img": None
    }
