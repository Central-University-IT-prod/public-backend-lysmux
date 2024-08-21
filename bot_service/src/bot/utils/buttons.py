from aiogram.fsm.state import State
from aiogram_dialog import StartMode
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.kbd import Start, SwitchTo, Cancel
from aiogram_dialog.widgets.text import Const

from bot.logic.dialogs.general.states import GeneralStates
from bot.multimedia.inline_texts import common as kb_texts

MENU_BTN_ID = "menu_btn"
BACK_BTN_ID = "back_btn"
CANCEL_BTN_ID = "cancel_btn"


def get_menu_button(
        when: WhenCondition | None = None
) -> Start:
    return Start(
        Const(kb_texts.MENU),
        id=MENU_BTN_ID,
        state=GeneralStates.menu,
        mode=StartMode.RESET_STACK,
        when=when
    )


def get_back_button(state: State) -> SwitchTo:
    return SwitchTo(
        Const(kb_texts.BACK),
        id=BACK_BTN_ID,
        state=state
    )


def get_cancel_button() -> Cancel:
    return Cancel(
        Const(kb_texts.CANCEL),
        id=CANCEL_BTN_ID
    )
