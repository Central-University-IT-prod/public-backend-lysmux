import operator

from aiogram_dialog import Window
from aiogram_dialog.widgets.common import sync_scroll
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Cancel, Button
from aiogram_dialog.widgets.text import Jinja, List, Format, Const

from bot.logic.dialogs.note.states import NoteState
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.multimedia.inline_texts import note as kb_texts
from .getter import data_getter
from .handlers import on_note_select, on_note_add

KB_WIDTH = 2
KB_HEIGHT = 1

GROUP_ID = "note_group"
SELECT_ID = "note_select"
SCROLL_ID = "note_scroll"
ADD_NOTE_BTN_ID = "add_note_btn"

window = Window(
    Jinja("notes/list_header.html"),
    Const(" "),
    List(
        field=Jinja("notes/list_item.html"),
        items="notes",
        page_size=KB_WIDTH * KB_HEIGHT,
        sep="\n" * 2,
        id=SCROLL_ID
    ),
    ScrollingGroup(
        Select(
            id=SELECT_ID,
            text=Format("{item.name}"),
            items="notes",
            item_id_getter=operator.attrgetter("id"),
            on_click=on_note_select,
            type_factory=str
        ),
        width=KB_WIDTH,
        height=KB_HEIGHT,
        id=GROUP_ID,
        on_page_changed=sync_scroll(scroll_id=SCROLL_ID)
    ),
    Button(
        id=ADD_NOTE_BTN_ID,
        text=Const(kb_texts.ADD_NOTE),
        on_click=on_note_add
    ),
    Cancel(
        text=Const(com_kb_texts.BACK)
    ),
    getter=data_getter,
    state=NoteState.list
)
