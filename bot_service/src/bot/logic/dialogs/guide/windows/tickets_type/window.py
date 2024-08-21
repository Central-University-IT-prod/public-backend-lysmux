from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, SwitchTo
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.guide.states import GuideStates
from bot.multimedia.inline_texts import guide as kb_texts
from bot.utils.buttons import get_back_button

TRAIN_TICKETS_BTN = "train_tickets"
AIR_TICKETS_BTN = "air_tickets"

window = Window(
    Jinja("guide/tickets_type.html"),
    Group(
        SwitchTo(
            id=AIR_TICKETS_BTN,
            text=Const(kb_texts.AIR_TICKETS),
            state=GuideStates.air_tickets
        ),
        SwitchTo(
            id=TRAIN_TICKETS_BTN,
            text=Const(kb_texts.TRAIN_TICKETS),
            state=GuideStates.train_tickets
        ),
        width=2
    ),
    get_back_button(state=GuideStates.action),
    state=GuideStates.tickets_type
)
