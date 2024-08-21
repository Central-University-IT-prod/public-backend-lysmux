from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Jinja

from bot.logic.dialogs.guide.states import GuideStates
from bot.utils.buttons import get_back_button
from .getter import data_getter

window = Window(
    Jinja("guide/route.html"),
    DynamicMedia(
        selector="route_img",
        when=F["route_img"].is_not(None)
    ),
    get_back_button(state=GuideStates.action),
    getter=data_getter,
    state=GuideStates.route
)
