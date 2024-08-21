from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.note_edit.states import NoteEditStates
from bot.multimedia.inline_texts import note as kb_texts
from bot.utils.buttons import get_cancel_button
from .handlers import ScopeHandler
from .ids import PUBLIC_SCOPE_BTN_ID, PRIVATE_SCOPE_BTN_ID

window = Window(
    Jinja("notes/scope.html"),
    Group(
        Button(
            id=PUBLIC_SCOPE_BTN_ID,
            text=Const(kb_texts.PUBLIC),
            on_click=ScopeHandler()
        ),
        Button(
            id=PRIVATE_SCOPE_BTN_ID,
            text=Const(kb_texts.PRIVATE),
            on_click=ScopeHandler()
        ),
        width=2
    ),
    get_cancel_button(),
    state=NoteEditStates.scope
)
