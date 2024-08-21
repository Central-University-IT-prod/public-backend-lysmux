from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.participant.states import ParticipantStates
from bot.multimedia.inline_texts import common as kb_texts
from bot.utils.buttons import get_back_button
from .handlers import on_participant_delete

CONFIRM_BTN_ID = "confirm_btn"
BACK_BTN_ID = "back_btn"

window = Window(
    Jinja("participants/confirm_delete.html"),
    Group(
        Button(
            id=CONFIRM_BTN_ID,
            text=Const(kb_texts.YES),
            on_click=on_participant_delete
        ),
        get_back_button(state=ParticipantStates.info),
        width=2
    ),
    state=ParticipantStates.confirm_delete
)
