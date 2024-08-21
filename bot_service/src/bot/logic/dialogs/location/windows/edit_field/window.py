from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.location.states import LocationStates
from bot.multimedia.inline_texts import location as kb_texts
from bot.utils.buttons import get_back_button
from .handlers import (
    on_edit_name,
    on_edit_start_date,
    on_edit_end_date,
    on_edit_location
)

EDIT_NAME_BTN_ID = "edit_name_btn"
EDIT_START_DATE_BTN_ID = "edit_start_btn"
EDIT_END_DATE_BTN_ID = "edit_end_btn"
EDIT_LOCATION_BTN_ID = "edit_loc_btn"

window = Window(
    Jinja("locations/edit.html"),
    Group(
        Button(
            id=EDIT_NAME_BTN_ID,
            text=Const(kb_texts.NAME),
            on_click=on_edit_name
        ),
        Button(
            id=EDIT_LOCATION_BTN_ID,
            text=Const(kb_texts.LOCATION),
            on_click=on_edit_location
        ),
        Button(
            id=EDIT_START_DATE_BTN_ID,
            text=Const(kb_texts.START_DATE),
            on_click=on_edit_start_date
        ),
        Button(
            id=EDIT_END_DATE_BTN_ID,
            text=Const(kb_texts.END_DATE),
            on_click=on_edit_end_date
        ),
        width=2
    ),
    get_back_button(state=LocationStates.info),
    state=LocationStates.edit_field
)
