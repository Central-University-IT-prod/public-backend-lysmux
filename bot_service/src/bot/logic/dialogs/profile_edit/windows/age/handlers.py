from typing import Any

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from bot.logic.dialogs.profile_edit.states import ProfileEditStates
from bot.utils.ce_handler import CEHandler
from bot.utils.template_engine import render_template

MAX_AGE = 200
MIN_AGE = 1


class AgeHandler(CEHandler):
    async def validate(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> bool:
        if not event.text.isdigit():
            return False

        age = int(event.text)
        if age < MIN_AGE:
            return False
        if age > MAX_AGE:
            return False

        return True

    async def on_validation_error(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        await event.answer(
            text=render_template("profile/errors/invalid_age.html")
        )

    async def process_create(
            self,
            event: Message,
            manager: DialogManager,
            source: MessageInput,
            data: Any
    ) -> None:
        manager.dialog_data["age"] = int(event.text)
        await manager.switch_to(
            state=ProfileEditStates.bio
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
                "age": int(event.text)
            }
        )
