from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.note.states import NoteState
from bot.multimedia.inline_texts import common as kb_texts
from bot.utils.buttons import get_back_button
from .handlers import on_note_delete

CONFIRM_BTN_ID = "confirm_btn"

window = Window(
    Jinja("notes/confirm_delete.html"),
    Group(
        Button(
            id=CONFIRM_BTN_ID,
            text=Const(kb_texts.YES),
            on_click=on_note_delete
        ),
        get_back_button(state=NoteState.info),
        width=2
    ),
    state=NoteState.confirm_delete
)
