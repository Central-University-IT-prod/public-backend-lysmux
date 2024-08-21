from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.guide.states import GuideStates
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.multimedia.inline_texts import guide as gui_kb_texts
from bot.utils.aiod_widgets import SwitchInlineCurChatQuery
from bot.utils.buttons import get_back_button
from .handelrs import on_location, on_prev

FROM_PREV_LOCATION = "route_from_prev"

window = Window(
    Jinja("guide/route_from.html"),
    SwitchInlineCurChatQuery(
        text=Const(com_kb_texts.SEARCH),
        switch_inline_query=Const("")
    ),
    Button(
        id=FROM_PREV_LOCATION,
        text=Const(gui_kb_texts.BY_PREV_LOCATION),
        on_click=on_prev
    ),
    MessageInput(
        func=on_location,
        content_types=ContentType.LOCATION
    ),
    get_back_button(state=GuideStates.action),
    state=GuideStates.route_from
)
