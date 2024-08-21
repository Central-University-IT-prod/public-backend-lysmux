from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button, SwitchTo
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.location.states import LocationStates
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.multimedia.inline_texts import location as loc_kb_texts
from bot.utils.buttons import get_back_button
from .getter import data_getter
from .handlers import show_guide

GUIDE_BTN_ID = "guide_btn"
EDIT_BTN_ID = "edit_btn"
DELETE_BTN_ID = "delete_btn"

window = Window(
    Jinja("locations/info.html"),
    Button(
        id=GUIDE_BTN_ID,
        text=Const(loc_kb_texts.GUIDE),
        on_click=show_guide
    ),
    Group(
        SwitchTo(
            id=EDIT_BTN_ID,
            text=Const(com_kb_texts.EDIT),
            state=LocationStates.edit_field
        ),
        SwitchTo(
            id=DELETE_BTN_ID,
            text=Const(com_kb_texts.DELETE),
            state=LocationStates.confirm_delete
        ),
        width=2,
        when="user_is_owner",
    ),
    get_back_button(state=LocationStates.list),
    getter=data_getter,
    state=LocationStates.info
)
