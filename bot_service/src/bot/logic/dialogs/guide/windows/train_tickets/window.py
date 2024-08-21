from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import (
    Row,
    PrevPage,
    FirstPage,
    CurrentPage,
    NextPage,
    LastPage, Url
)
from aiogram_dialog.widgets.text import Jinja, Format, List, Const

from bot.logic.dialogs.guide.states import GuideStates
from bot.utils.buttons import get_back_button
from .getter import data_getter

ITEMS_PER_PAGE = 2
LIST_ID = "train_tickets_list"

window = Window(
    Jinja("guide/train_tickets.html"),
    Const(" "),
    List(
        id=LIST_ID,
        field=Jinja("guide/train_ticket.html"),
        items="tickets",
        sep="\n" * 2,
        page_size=ITEMS_PER_PAGE
    ),
    Row(
        FirstPage(scroll=LIST_ID, text=Format("{target_page1}")),
        PrevPage(scroll=LIST_ID),
        CurrentPage(scroll=LIST_ID),
        NextPage(scroll=LIST_ID),
        LastPage(scroll=LIST_ID, text=Format("{target_page1}")),
        when=F["tickets"].len() > 0
    ),
    Url(
        text=Const("Купить билет"),
        url=Format("https://ticket.rzd.ru/searchresults/v/1/{from_bus_code}/{to_bus_code}/{date}"),
        when=F["tickets"].len() > 0
    ),
    get_back_button(state=GuideStates.tickets_type),
    getter=data_getter,
    state=GuideStates.train_tickets
)
