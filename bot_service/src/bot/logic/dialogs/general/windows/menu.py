from aiogram_dialog import Window, StartMode
from aiogram_dialog.widgets.kbd import Group, Start
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.general.states import GeneralStates
from bot.logic.dialogs.profile.states import ProfileStates
from bot.logic.dialogs.travel.states import TravelStates
from bot.multimedia.inline_texts import menu as kb_texts

TRAVELS_BTN_ID = "travels_btn"
PROFILE_BTN_ID = "profile_btn"

window = Window(
    Jinja("general/menu.html"),
    Group(
        Start(
            Const(kb_texts.TRAVELS),
            id=TRAVELS_BTN_ID,
            state=TravelStates.list,
            mode=StartMode.RESET_STACK
        ),
        Start(
            Const(kb_texts.PROFILE),
            id=PROFILE_BTN_ID,
            state=ProfileStates.info,
            mode=StartMode.RESET_STACK
        ),
        width=2
    ),
    state=GeneralStates.menu
)
