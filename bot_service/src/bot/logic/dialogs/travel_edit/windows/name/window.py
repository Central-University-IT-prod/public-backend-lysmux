from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Jinja

from bot.logic.dialogs.travel_edit.states import TravelEditStates
from bot.utils.buttons import get_cancel_button
from .handlers import NameHandler

window = Window(
    Jinja("travels/name.html"),
    MessageInput(
        func=NameHandler(),
        content_types=ContentType.TEXT
    ),
    get_cancel_button(),
    state=TravelEditStates.name
)
