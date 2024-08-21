from datetime import date
from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedCalendar

from bot.logic.dialogs.location_edit.states import LocationEditStates
from bot.utils.ce_handler import CEHandler
from bot.utils.template_engine import render_template
from travel_api import TravelApi


class DateHandler(CEHandler):
    async def validate(
            self,
            event: CallbackQuery,
            manager: DialogManager,
            source: ManagedCalendar,
            data: date
    ) -> bool:
        if location_id := manager.start_data.get("location_id"):
            travel_api: TravelApi = manager.middleware_data["travel_api"]
            location = await travel_api.get_travel_location(location_id)
            start_date = location.start_date
        else:
            start_date_iso: str = manager.dialog_data["start_date"]
            start_date = date.fromisoformat(start_date_iso)
        return data >= start_date

    async def on_validation_error(
            self,
            event: CallbackQuery,
            manager: DialogManager,
            source: Any,
            data: Any
    ) -> None:
        await event.message.answer(
            text=render_template("locations/errors/invalid_end_date.html")
        )

    async def process_create(
            self,
            event: CallbackQuery,
            manager: DialogManager,
            source: ManagedCalendar,
            data: date
    ) -> None:
        manager.dialog_data["end_date"] = data.isoformat()
        await manager.switch_to(
            state=LocationEditStates.location
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
            "end_date": data.isoformat()
        })
