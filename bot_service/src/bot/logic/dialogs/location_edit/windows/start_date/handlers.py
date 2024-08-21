from datetime import date

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCalendar

from bot.logic.dialogs.location_edit.states import LocationEditStates
from bot.utils.ce_handler import CEHandler


class DateHandler(CEHandler):
    async def process_create(
            self,
            event: CallbackQuery,
            manager: DialogManager,
            source: ManagedCalendar,
            data: date
    ) -> None:
        manager.dialog_data["start_date"] = data.isoformat()
        await manager.switch_to(
            state=LocationEditStates.end_date
        )

    async def process_edit(
            self,
            event: CallbackQuery,
            manager: DialogManager,
            source: ManagedCalendar,
            data: date
    ) -> None:
        await manager.done({
            "action": "edit",
            "start_date": data.isoformat()
        })
