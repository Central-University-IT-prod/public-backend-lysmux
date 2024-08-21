from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from bot.logic.dialogs.location.states import LocationStates
from bot.logic.dialogs.location_edit.states import LocationEditStates


async def on_location_select(
        event: CallbackQuery,
        select: Select,
        dialog_manager: DialogManager,
        location_id: str,
) -> None:
    dialog_manager.dialog_data["sel_location_id"] = location_id

    await dialog_manager.switch_to(
        state=LocationStates.info
    )


async def on_location_add(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager,
) -> None:
    travel_id: str = dialog_manager.start_data["travel_id"]

    await dialog_manager.start(
        state=LocationEditStates.name,
        data={
            "travel_id": travel_id
        }
    )
