from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, SwitchTo
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.note.states import NoteState
from bot.multimedia.inline_texts import common as kb_texts
from bot.utils.buttons import get_back_button
from .getter import data_getter

EDIT_BTN_ID = "note_edit_btn"
DELETE_BTN_ID = "note_delete_btn"

window = Window(
    Jinja("notes/info.html"),
    DynamicMedia(
        selector="media",
        when=F["media"].is_not(None)
    ),
    Group(
        SwitchTo(
            id=EDIT_BTN_ID,
            text=Const(kb_texts.EDIT),
            state=NoteState.edit_field
        ),
        SwitchTo(
            id=DELETE_BTN_ID,
            text=Const(kb_texts.DELETE),
            state=NoteState.confirm_delete
        ),
        width=2
    ),
    get_back_button(state=NoteState.list),
    getter=data_getter,
    state=NoteState.info
)
