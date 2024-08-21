import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.kbd import Cancel, ScrollingGroup, Select, Button
from aiogram_dialog.widgets.text import Const, Jinja, List, Format

from bot.logic.dialogs.location.states import LocationStates
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.multimedia.inline_texts import location as loc_kb_texts
from .getter import data_getter
from .handlers import on_location_select, on_location_add

KB_WIDTH = 2
KB_HEIGHT = 1

ADD_LOCATION_ID = "add_location_btn"
GROUP_ID = "list_group"
SELECT_ID = "list_select"
SCROLL_ID = "list_scroll"

window = Window(
    Jinja("locations/list_header.html"),
    Const(" "),
    List(
        field=Jinja("locations/list_item.html"),
        items="locations",
        page_size=KB_WIDTH * KB_HEIGHT,
        sep="\n" * 2,
        id=SCROLL_ID
    ),
    ScrollingGroup(
        Select(
            id=SELECT_ID,
            text=Format("{item.name}"),
            items="locations",
            item_id_getter=operator.attrgetter("id"),
            on_click=on_location_select,
            type_factory=str
        ),
        width=KB_WIDTH,
        height=KB_HEIGHT,
        id=GROUP_ID,
        on_page_changed=sync_scroll(scroll_id=SCROLL_ID)
    ),
    Button(
        id=ADD_LOCATION_ID,
        text=Const(loc_kb_texts.ADD_LOCATION),
        on_click=on_location_add
    ),
    Cancel(
        text=Const(com_kb_texts.BACK)
    ),
    getter=data_getter,
    state=LocationStates.list
)
