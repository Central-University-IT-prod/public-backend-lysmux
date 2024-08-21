from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.travel_edit.states import TravelEditStates


async def on_edit_name(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    travel_id: str = manager.dialog_data["sel_travel_id"]
    await manager.start(
        state=TravelEditStates.name,
        data={
            "edit": True,
            "travel_id": travel_id
        }
    )


async def on_edit_description(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    travel_id: str = manager.dialog_data["sel_travel_id"]
    await manager.start(
        state=TravelEditStates.description,
        data={
            "edit": True,
            "travel_id": travel_id
        }
    )
