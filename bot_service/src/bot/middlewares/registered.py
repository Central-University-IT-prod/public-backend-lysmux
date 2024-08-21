from typing import Callable, Dict, Any, Awaitable

from aiogram.types import (
    TelegramObject,
    Message,
    CallbackQuery
)
from aiogram_dialog import DialogManager, StartMode

from bot.logic.dialogs.profile.states import ProfileStates


async def is_user_registered(
        handler: Callable[
            [TelegramObject, Dict[str, Any]],
            Awaitable[Any]
        ],
        event: TelegramObject,
        data: Dict[str, Any]
) -> Any:
    if isinstance(event, Message | CallbackQuery):
        user = data["user"]
        dialog_manager: DialogManager = data["dialog_manager"]

        if user is None:
            await dialog_manager.start(
                state=ProfileStates.info,
                mode=StartMode.RESET_STACK
            )
        else:
            return await handler(event, data)
    else:
        return await handler(event, data)
