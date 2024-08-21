from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.guide.states import GuideStates


async def show_guide(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
) -> None:
    travel_id: str = dialog_manager.start_data["travel_id"]
    location_id: str = dialog_manager.dialog_data["sel_location_id"]
    await dialog_manager.start(
        state=GuideStates.action,
        data={
            "travel_id": travel_id,
            "location_id": location_id
        }
    )
