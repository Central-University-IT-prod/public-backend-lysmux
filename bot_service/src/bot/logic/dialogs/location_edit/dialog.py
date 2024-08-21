from aiogram_dialog import Dialog, DialogManager

from bot.middlewares import is_user_registered
from travel_api import TravelApi
from travel_api.schemas.location import (
    TravelLocationCreate, TravelLocationUpdate
)
from .windows import windows


async def process_close(
        result: dict,
        dialog_manager: DialogManager
) -> None:
    if not result:
        return

    travel_api: TravelApi = dialog_manager.middleware_data["travel_api"]

    match result.get("action"):
        case "create":
            travel_id: str = dialog_manager.start_data["travel_id"]
            await travel_api.add_travel_location(
                TravelLocationCreate(
                    travel_id=travel_id,
                    name=result["name"],
                    start_date=result["start_date"],
                    end_date=result["end_date"],
                    latitude=result["latitude"],
                    longitude=result["longitude"],
                )
            )
        case "edit":
            location_id: str = dialog_manager.start_data["location_id"]
            await travel_api.update_travel_location(
                location_id=location_id,
                update_schema=TravelLocationUpdate(
                    name=result.get("name"),
                    start_date=result.get("start_date"),
                    end_date=result.get("end_date"),
                    latitude=result.get("latitude"),
                    longitude=result.get("longitude"),
                )
            )


dialog = Dialog(*windows, on_close=process_close)
dialog.message.middleware(is_user_registered)
dialog.callback_query.middleware(is_user_registered)

