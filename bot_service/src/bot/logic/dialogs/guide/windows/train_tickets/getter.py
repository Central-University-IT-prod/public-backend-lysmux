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
    from_loc_type: str = dialog_manager.dialog_data["from"]
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

    from_city_code = await api_gateway.train_tickets_api.get_city_code(
        city=from_location.name
    )
    to_city_code = await api_gateway.train_tickets_api.get_city_code(
        city=to_location.name
    )

    if from_city_code and to_city_code:
        tickets = await api_gateway.train_tickets_api.get_tickets(
            from_station=from_city_code.code,
            to_station=to_city_code.code,
            departure_date=to_travel_location.start_date
        )

        return {
            "tickets": tickets,
            "from_bus_code": from_city_code.bus_code,
            "to_bus_code": to_city_code.bus_code,
            "date": to_travel_location.start_date,
        }
    return {
        "tickets": [],
    }
