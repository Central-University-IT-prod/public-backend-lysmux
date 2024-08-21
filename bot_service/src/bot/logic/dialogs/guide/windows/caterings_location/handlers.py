from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.guide.states import GuideStates


async def on_location(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager
) -> None:
    manager.dialog_data["latitude"] = message.location.latitude
    manager.dialog_data["longitude"] = message.location.longitude
    manager.dialog_data["from"] = "current"

    await manager.switch_to(GuideStates.caterings)


async def on_prev(
        callback_query: CallbackQuery,
        button: Button,
        manager: DialogManager
) -> None:
    manager.dialog_data["from"] = "prev"

    await manager.switch_to(GuideStates.caterings)
