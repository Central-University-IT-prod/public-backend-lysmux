from aiogram.types import User as TgUser
from aiogram_dialog import Dialog, DialogManager

from travel_api import TravelApi
from travel_api.schemas.user import User, UserUpdate
from .windows import windows


async def process_close(
        result: dict,
        dialog_manager: DialogManager
):
    if not result:
        return

    event_from_user: TgUser = dialog_manager.middleware_data["event_from_user"]
    travel_api: TravelApi = dialog_manager.middleware_data["travel_api"]

    match result.get("action"):
        case "create":
            await travel_api.create_user(
                User(
                    id=event_from_user.id,
                    name=result["name"],
                    age=result["age"],
                    bio=result["bio"],
                    latitude=result["latitude"],
                    longitude=result["longitude"]
                )
            )
        case "edit":
            await travel_api.update_user(
                user_id=event_from_user.id,
                update_schema=UserUpdate(
                    name=result.get("name"),
                    age=result.get("age"),
                    bio=result.get("bio"),
                    latitude=result.get("latitude"),
                    longitude=result.get("longitude"),
                )
            )


dialog = Dialog(*windows, on_close=process_close)
