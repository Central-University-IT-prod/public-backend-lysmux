from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from bot.logic.dialogs.profile_edit.states import ProfileEditStates
from bot.utils.ce_handler import CEHandler
from bot.utils.template_engine import render_template

MIN_BIO_LEN = 5
MAX_BIO_LEN = 150


class BioHandler(CEHandler):
    async def validate(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> bool:
        return MIN_BIO_LEN <= len(event.text) <= MAX_BIO_LEN

    async def on_validation_error(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        await event.answer(
            text=render_template("profile/errors/invalid_bio.html")
        )

    async def process_create(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        manager.dialog_data["bio"] = event.text
        await manager.switch_to(
            state=ProfileEditStates.location
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
                "bio": event.text
            }
        )
