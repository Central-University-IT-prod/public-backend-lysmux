from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from bot.logic.dialogs.travel.states import TravelStates
from bot.logic.dialogs.travel_edit.states import TravelEditStates


async def on_travel_select(
        event: CallbackQuery,
        select: Select,
        dialog_manager: DialogManager,
        travel_id: str,
) -> None:
    dialog_manager.dialog_data["sel_travel_id"] = travel_id

    await dialog_manager.switch_to(
        state=TravelStates.info
    )


async def on_travel_add(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(
        state=TravelEditStates.name
    )
