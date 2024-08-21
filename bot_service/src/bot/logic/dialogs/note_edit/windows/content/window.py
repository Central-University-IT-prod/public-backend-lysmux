from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Jinja

from bot.logic.dialogs.note_edit.states import NoteEditStates
from bot.utils.buttons import get_cancel_button
from .handlers import ContentHandler

window = Window(
    Jinja("notes/content.html"),
    MessageInput(
        func=ContentHandler(),
        content_types=(
            ContentType.TEXT,
            ContentType.VIDEO,
            ContentType.PHOTO,
            ContentType.DOCUMENT,
        )
    ),
    get_cancel_button(),
    state=NoteEditStates.content
)
