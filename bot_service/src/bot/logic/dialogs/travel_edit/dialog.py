from typing import Any

from aiogram.types import User
from aiogram_dialog import Dialog, DialogManager

from bot.middlewares import is_user_registered
from travel_api import TravelApi
from travel_api.schemas.travel import TravelCreate, TravelUpdate
from .windows import windows


async def process_close(
        result: dict[str, Any],
        manager: DialogManager
) -> None:
    if not result:
        return

    travel_api: TravelApi = manager.middleware_data["travel_api"]

    match result.get("action"):
        case "create":
            user: User = manager.middleware_data["event_from_user"]
            await travel_api.add_travel(
                TravelCreate(
                    owner_id=user.id,
                    name=result["name"],
                    description=result["description"]
                )
            )
        case "edit":
            travel_id: str = manager.start_data["travel_id"]
            await travel_api.update_travel(
                travel_id=travel_id,
                update_schema=TravelUpdate(
                    name=result.get("name"),
                    description=result.get("description")
                )
            )


dialog = Dialog(*windows, on_close=process_close)
dialog.message.middleware(is_user_registered)
dialog.callback_query.middleware(is_user_registered)
