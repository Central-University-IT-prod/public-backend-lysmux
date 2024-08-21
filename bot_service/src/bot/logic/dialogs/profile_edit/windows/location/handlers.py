from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from bot.utils.ce_handler import CEHandler


class LocationHandler(CEHandler):
    async def process_create(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        location = event.location
        name: str = manager.dialog_data["name"]
        age: int = manager.dialog_data["age"]
        bio: str = manager.dialog_data["bio"]

        await manager.done(
            {
                "action": "create",
                "name": name,
                "age": age,
                "bio": bio,
                "latitude": location.latitude,
                "longitude": location.longitude,
            }
        )

    async def process_edit(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        location = event.location

        await manager.done(
            {
                "action": "edit",
                "latitude": location.latitude,
                "longitude": location.longitude,
            }
        )
