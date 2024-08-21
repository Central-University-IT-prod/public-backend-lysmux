from typing import Any

from aiogram.types import User
from aiogram_dialog import Dialog, DialogManager

from bot.middlewares import is_user_registered
from travel_api import TravelApi
from travel_api.schemas.note import NoteCreate, NoteUpdate
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
            travel_id: str = manager.start_data["travel_id"]
            user: User = manager.middleware_data["event_from_user"]
            await travel_api.add_note(
                create_schema=NoteCreate(
                    owner_id=user.id,
                    name=result["name"],
                    is_public=result["is_public"],
                    file_id=result.get("file_id"),
                    content_type=result.get("content_type"),
                    text=result.get("text"),
                    travel_id=travel_id
                )
            )
        case "edit":
            note_id: str = manager.start_data["note_id"]
            await travel_api.update_note(
                note_id=note_id,
                update_schema=NoteUpdate(
                    name=result.get("name"),
                    content_type=result.get("content_type"),
                    file_id=result.get("file_id"),
                    text=result.get("text"),
                    is_public=result.get("is_public"),
                )
            )


dialog = Dialog(*windows, on_close=process_close)
dialog.message.middleware(is_user_registered)
dialog.callback_query.middleware(is_user_registered)
