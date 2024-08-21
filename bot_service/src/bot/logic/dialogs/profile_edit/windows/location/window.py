from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.profile_edit.states import ProfileEditStates
from bot.multimedia.inline_texts import common as kb_texts
from bot.utils.aiod_widgets import SwitchInlineCurChatQuery
from bot.utils.buttons import get_cancel_button
from .handlers import LocationHandler

window = Window(
    Jinja("profile/location.html"),
    SwitchInlineCurChatQuery(
        text=Const(kb_texts.SEARCH),
        switch_inline_query=Const("")
    ),
    MessageInput(
        func=LocationHandler(),
        content_types=ContentType.LOCATION
    ),
    get_cancel_button(),
    state=ProfileEditStates.location
)
