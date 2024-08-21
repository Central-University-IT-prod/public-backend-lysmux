from aiogram_dialog import Dialog

from bot.middlewares import is_user_registered
from .windows import windows

dialog = Dialog(*windows)
dialog.message.middleware(is_user_registered)
dialog.callback_query.middleware(is_user_registered)
