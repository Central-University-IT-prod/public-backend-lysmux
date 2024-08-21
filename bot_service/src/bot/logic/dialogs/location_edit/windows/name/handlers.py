from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from bot.logic.dialogs.location_edit.states import LocationEditStates
from bot.utils.ce_handler import CEHandler
from bot.utils.template_engine import render_template

MIN_NAME_LEN = 3
MAX_NAME_LEN = 15


class NameHandler(CEHandler):
    async def validate(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> bool:
        return MIN_NAME_LEN <= len(event.text) <= MAX_NAME_LEN

    async def on_validation_error(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        await event.answer(
            text=render_template("locations/errors/invalid_name.html")
        )

    async def process_create(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        manager.dialog_data["name"] = event.text
        await manager.switch_to(
            state=LocationEditStates.start_date
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
                "name": event.text
            }
        )
