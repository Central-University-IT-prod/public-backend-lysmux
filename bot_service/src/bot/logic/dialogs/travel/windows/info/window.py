from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button, SwitchTo
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.travel.states import TravelStates
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.multimedia.inline_texts import travels as trav_kb_texts
from bot.utils.buttons import get_back_button
from .getter import data_getter
from .handlers import (
    show_notes,
    show_locations,
    show_participants
)

LOCATIONS_BTN_ID = "travel_locations_btn"
PARTICIPANTS_BTN_ID = "travel_participants_btn"
NOTES_BTN_ID = "travel_notes_btn"
EDIT_BTN_ID = "travel_edit_btn"
DELETE_BTN_ID = "travel_delete_btn"

window = Window(
    Jinja("travels/info.html"),
    Group(
        Button(
            id=LOCATIONS_BTN_ID,
            text=Const(trav_kb_texts.LOCATIONS),
            on_click=show_locations
        ),
        Button(
            id=PARTICIPANTS_BTN_ID,
            text=Const(trav_kb_texts.PARTICIPANTS),
            on_click=show_participants
        ),
        Button(
            id=NOTES_BTN_ID,
            text=Const(trav_kb_texts.NOTES),
            on_click=show_notes
        ),
        width=2
    ),
    Group(
        SwitchTo(
            id=EDIT_BTN_ID,
            text=Const(com_kb_texts.EDIT),
            state=TravelStates.edit_field
        ),
        SwitchTo(
            id=DELETE_BTN_ID,
            text=Const(com_kb_texts.DELETE),
            state=TravelStates.confirm_delete
        ),
        width=2,
        when="user_is_owner",
    ),
    get_back_button(state=TravelStates.list),
    getter=data_getter,
    state=TravelStates.info
)
