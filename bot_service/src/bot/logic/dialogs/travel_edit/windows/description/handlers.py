from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from bot.utils.ce_handler import CEHandler
from bot.utils.template_engine import render_template

MIN_DESC_LEN = 5
MAX_DESC_LEN = 150


class DescriptionHandler(CEHandler):
    async def validate(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> bool:
        return MIN_DESC_LEN <= len(event.text) <= MAX_DESC_LEN

    async def on_validation_error(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        await event.answer(
            text=render_template("travels/errors/invalid_description.html")
        )

    async def process_create(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        name: str = manager.dialog_data["name"]

        await manager.done(
            {
                "action": "create",
                "name": name,
                "description": event.text,
            }
        )

    async def process_edit(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        await manager.done(
            {
                "action": "edit",
                "description": event.text
            }
        )
