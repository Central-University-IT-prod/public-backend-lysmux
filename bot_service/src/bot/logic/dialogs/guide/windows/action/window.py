from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, Cancel, SwitchTo
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.guide.states import GuideStates
from bot.multimedia.inline_texts import common as com_kb_texts
from bot.multimedia.inline_texts import guide as kb_texts

ROUTE_BTN_ID = "route_btn"
WEATHER_BTN_ID = "weather_btn"
TICKETS_BTN_ID = "tickets_btn"
HOTELS_BTN_ID = "hotels_btn"
CATERINGS_BTN_ID = "caterings_btn"
INTERESTING_PLACES_BTN_ID = "inter_places_btn"

window = Window(
    Jinja("guide/action.html"),
    Group(
        SwitchTo(
            id=ROUTE_BTN_ID,
            text=Const(kb_texts.ROUTE),
            state=GuideStates.route_from
        ),
        SwitchTo(
            id=WEATHER_BTN_ID,
            text=Const(kb_texts.WEATHER),
            state=GuideStates.weather
        ),
        SwitchTo(
            id=TICKETS_BTN_ID,
            text=Const(kb_texts.TICKETS),
            state=GuideStates.tickets_from
        ),
        SwitchTo(
            id=HOTELS_BTN_ID,
            text=Const(kb_texts.HOTELS),
            state=GuideStates.hotels
        ),
        SwitchTo(
            id=CATERINGS_BTN_ID,
            text=Const(kb_texts.CATERINGS),
            state=GuideStates.caterings_location
        ),
        SwitchTo(
            id=INTERESTING_PLACES_BTN_ID,
            text=Const(kb_texts.INTERESTED_PLACES),
            state=GuideStates.attractions
        ),
        width=2
    ),
    Cancel(
        text=Const(com_kb_texts.BACK)
    ),
    state=GuideStates.action
)
