from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.travel.states import TravelStates
from bot.multimedia.inline_texts import travels as kb_texts
from bot.utils.buttons import get_back_button
from .handlers import (
    on_edit_name,
    on_edit_description
)

EDIT_NAME_BTN_ID = "edit_name_btn"
EDIT_DESC_BTN_ID = "edit_desc_btn"

window = Window(
    Jinja("travels/edit.html"),
    Group(
        Button(
            id=EDIT_NAME_BTN_ID,
            text=Const(kb_texts.NAME),
            on_click=on_edit_name
        ),
        Button(
            id=EDIT_DESC_BTN_ID,
            text=Const(kb_texts.DESCRIPTION),
            on_click=on_edit_description
        ),
        width=2
    ),
    get_back_button(state=TravelStates.info),
    state=TravelStates.edit_field
)
