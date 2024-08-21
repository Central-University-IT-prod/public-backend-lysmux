from datetime import date

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Calendar, CalendarConfig
from aiogram_dialog.widgets.text import Jinja

from bot.logic.dialogs.location_edit.states import LocationEditStates
from bot.utils.buttons import get_cancel_button
from .handlers import DateHandler

CALENDAR_ID = "end_calendar"

window = Window(
    Jinja("locations/end_date.html"),
    Calendar(
        id=CALENDAR_ID,
        on_click=DateHandler(),
        config=CalendarConfig(
            min_date=date.today()
        )
    ),
    get_cancel_button(),
    state=LocationEditStates.end_date
)
