import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Button
from aiogram_dialog.widgets.text import Jinja, List, Format, Const

from bot.logic.dialogs.travel.states import TravelStates
from bot.multimedia.inline_texts import travels as kb_texts
from bot.utils.buttons import get_menu_button
from .getter import data_getter
from .handlers import on_travel_select, on_travel_add

KB_WIDTH = 2
KB_HEIGHT = 1

GROUP_ID = "list_group"
SELECT_ID = "list_select"
SCROLL_ID = "list_scroll"

ADD_TRAVEL_BTN_ID = "add_travel"

window = Window(
    Jinja("travels/list_header.html"),
    Const(" "),
    List(
        field=Jinja("travels/list_item.html"),
        items="travels",
        page_size=KB_WIDTH * KB_HEIGHT,
        sep="\n" * 2,
        id=SCROLL_ID
    ),
    ScrollingGroup(
        Select(
            id=SELECT_ID,
            text=Format("{item.name}"),
            items="travels",
            item_id_getter=operator.attrgetter("id"),
            on_click=on_travel_select,
            type_factory=str
        ),
        width=KB_WIDTH,
        height=KB_HEIGHT,
        id=GROUP_ID,
        on_page_changed=sync_scroll(scroll_id=SCROLL_ID)
    ),
    Button(
        id=ADD_TRAVEL_BTN_ID,
        text=Const(kb_texts.ADD_TRAVEL),
        on_click=on_travel_add
    ),
    get_menu_button(),
    getter=data_getter,
    state=TravelStates.list
)
