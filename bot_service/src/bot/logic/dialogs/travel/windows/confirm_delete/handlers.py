from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.travel.states import TravelStates
from bot.multimedia.inline_texts import travels as inline_texts
from travel_api import TravelApi


async def on_travel_delete(
        event: CallbackQuery,
        select: Button,
        dialog_manager: DialogManager,
) -> None:
    travel_api: TravelApi = dialog_manager.middleware_data["travel_api"]
    travel_id: str = dialog_manager.dialog_data["sel_travel_id"]

    await travel_api.delete_travel(travel_id)
    await event.answer(inline_texts.DELETED)
    await dialog_manager.switch_to(state=TravelStates.list)
