from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.location.states import LocationStates
from bot.multimedia.inline_texts import common as kb_texts
from bot.utils.buttons import get_back_button
from .handlers import on_location_delete

CONFIRM_BTN_ID = "confirm_btn"
BACK_BTN_ID = "back_btn"

window = Window(
    Jinja("locations/confirm_delete.html"),
    Group(
        Button(
            id=CONFIRM_BTN_ID,
            text=Const(kb_texts.YES),
            on_click=on_location_delete
        ),
        get_back_button(state=LocationStates.info),
        width=2
    ),
    state=LocationStates.confirm_delete
)
