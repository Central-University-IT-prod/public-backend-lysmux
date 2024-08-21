from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, SwitchTo
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.profile.states import ProfileStates
from bot.logic.dialogs.profile_edit.states import ProfileEditStates
from bot.multimedia.inline_texts import profile as kb_texts
from bot.utils.buttons import get_menu_button
from .getter import data_getter

CREATE_BTN_ID = "create_btn"
EDIT_BTN_ID = "edit_btn"

window = Window(
    Jinja("profile/info.html"),
    Start(
        id=CREATE_BTN_ID,
        text=Const(kb_texts.CREATE_PROFILE),
        state=ProfileEditStates.name,
        when=F["user"].is_(None)
    ),
    SwitchTo(
        id=EDIT_BTN_ID,
        text=Const(kb_texts.EDIT_PROFILE),
        state=ProfileStates.edit_field,
        when=F["user"].is_not(None)
    ),
    get_menu_button(when=F["user"].is_not(None)),  # noqa  # hide menu but when user is not registered
    getter=data_getter,
    state=ProfileStates.info
)
