from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.participant.states import ParticipantStates
from bot.multimedia.inline_texts import participants as kb_texts
from bot.utils.aiod_widgets import RequestUser
from bot.utils.buttons import get_back_button
from .handlers import on_participant

REQUEST_ID = 1

window = Window(
    Jinja("participants/add.html"),
    RequestUser(
        text=Const(kb_texts.SELECT_USER),
        request_id=REQUEST_ID,
        user_is_bot=False
    ),
    get_back_button(state=ParticipantStates.list),
    MessageInput(
        func=on_participant,
        content_types=ContentType.USERS_SHARED
    ),
    markup_factory=ReplyKeyboardFactory(
        resize_keyboard=True,
        one_time_keyboard=True
    ),
    state=ParticipantStates.add
)
