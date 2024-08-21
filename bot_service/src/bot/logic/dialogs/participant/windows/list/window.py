import operator

from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.kbd import Cancel, ScrollingGroup, Select, SwitchTo
from aiogram_dialog.widgets.text import Const, Jinja, List, Format

from bot.logic.dialogs.participant.states import ParticipantStates
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.multimedia.inline_texts import participants as par_kb_texts
from .getter import data_getter
from .handlers import on_participant_select

KB_WIDTH = 2
KB_HEIGHT = 3

ADD_PARTICIPANT_ID = "add_participant_btn"
GROUP_ID = "list_group"
SELECT_ID = "list_select"
SCROLL_ID = "list_scroll"

window = Window(
    Jinja("participants/list_header.html"),
    Const(" "),
    List(
        field=Jinja("participants/list_item.html"),
        items="participants",
        page_size=KB_WIDTH * KB_HEIGHT,
        id=SCROLL_ID
    ),
    ScrollingGroup(
        Select(
            id=SELECT_ID,
            text=Format("{item.name}"),
            items="participants",
            item_id_getter=operator.attrgetter("id"),
            on_click=on_participant_select,
            type_factory=str
        ),
        width=KB_WIDTH,
        height=KB_HEIGHT,
        id=GROUP_ID,
        on_page_changed=sync_scroll(scroll_id=SCROLL_ID)
    ),
    SwitchTo(
        id=ADD_PARTICIPANT_ID,
        text=Const(par_kb_texts.ADD_PARTICIPANT),
        state=ParticipantStates.add,
        when=F["user_is_owner"]
    ),
    Cancel(
        text=Const(com_kb_texts.BACK)
    ),
    getter=data_getter,
    state=ParticipantStates.list
)
