from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.note.states import NoteState
from bot.multimedia.inline_texts import note as kb_texts
from bot.utils.buttons import get_back_button
from .handlers import (
    on_edit_name,
    on_edit_content,
    on_edit_scope
)

EDIT_NAME_BTN_ID = "edit_name_btn"
EDIT_CONTENT_BTN_ID = "edit_content_btn"
EDIT_SCOPE_BTN_ID = "edit_scope_btn"

window = Window(
    Jinja("notes/edit.html"),
    Group(
        Button(
            id=EDIT_NAME_BTN_ID,
            text=Const(kb_texts.NAME),
            on_click=on_edit_name
        ),
        Button(
            id=EDIT_CONTENT_BTN_ID,
            text=Const(kb_texts.CONTENT),
            on_click=on_edit_content
        ),
        Button(
            id=EDIT_SCOPE_BTN_ID,
            text=Const(kb_texts.SCOPE),
            on_click=on_edit_scope
        ),
        width=2
    ),
    get_back_button(state=NoteState.info),
    state=NoteState.edit_field
)
