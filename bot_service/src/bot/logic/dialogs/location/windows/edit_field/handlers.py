from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.location_edit.states import LocationEditStates


async def on_edit_name(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    location_id: str = manager.dialog_data["sel_location_id"]
    await manager.start(
        state=LocationEditStates.name,
        data={
            "edit": True,
            "location_id": location_id
        }
    )


async def on_edit_start_date(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    location_id: str = manager.dialog_data["sel_location_id"]
    await manager.start(
        state=LocationEditStates.start_date,
        data={
            "edit": True,
            "location_id": location_id
        }
    )


async def on_edit_end_date(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    location_id: str = manager.dialog_data["sel_location_id"]
    await manager.start(
        state=LocationEditStates.end_date,
        data={
            "edit": True,
            "location_id": location_id
        }
    )


async def on_edit_location(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    location_id: str = manager.dialog_data["sel_location_id"]
    await manager.start(
        state=LocationEditStates.location,
        data={
            "edit": True,
            "location_id": location_id
        }
    )
