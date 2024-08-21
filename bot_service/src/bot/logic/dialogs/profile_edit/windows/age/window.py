from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Jinja

from bot.logic.dialogs.profile_edit.states import ProfileEditStates
from bot.utils.buttons import get_cancel_button
from .handlers import AgeHandler

window = Window(
    Jinja("profile/age.html"),
    MessageInput(
        func=AgeHandler(),
        content_types=ContentType.TEXT
    ),
    get_cancel_button(),
    state=ProfileEditStates.age
)
