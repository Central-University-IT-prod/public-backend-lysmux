from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.participant.states import ParticipantStates
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.utils.buttons import get_back_button
from .getter import data_getter

DELETE_BTN_ID = "delete_btn"

window = Window(
    Jinja("participants/info.html"),
    SwitchTo(
        id=DELETE_BTN_ID,
        text=Const(com_kb_texts.DELETE),
        state=ParticipantStates.confirm_delete,
        when=F["user_is_owner"] & (F["owner_id"] != F["participant_id"])
    ),
    get_back_button(state=ParticipantStates.list),
    getter=data_getter,
    state=ParticipantStates.info
)
