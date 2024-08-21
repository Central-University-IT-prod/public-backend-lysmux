from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start, Group
from aiogram_dialog.widgets.text import Jinja, Const

from bot.logic.dialogs.profile.states import ProfileStates
from bot.logic.dialogs.profile_edit.states import ProfileEditStates
from bot.multimedia.inline_texts import profile as kb_texts
from bot.utils.buttons import get_back_button
from .getter import data_getter

EDIT_NAME_BTN_ID = "edit_name_btn"
EDIT_AGE_BTN_ID = "edit_age_btn"
EDIT_BIO_BTN_ID = "edit_bio_btn"
EDIT_LOCATION_BTN_ID = "edit_loc_btn"

DATA = {
    "edit": True
}

window = Window(
    Jinja("profile/edit.html"),
    Group(
        Start(
            id=EDIT_NAME_BTN_ID,
            text=Const(kb_texts.NAME),
            state=ProfileEditStates.name,
            data=DATA
        ),
        Start(
            id=EDIT_AGE_BTN_ID,
            text=Const(kb_texts.AGE),
            state=ProfileEditStates.age,
            data=DATA
        ),
        Start(
            id=EDIT_BIO_BTN_ID,
            text=Const(kb_texts.BIO),
            state=ProfileEditStates.bio,
            data=DATA
        ),
        Start(
            id=EDIT_LOCATION_BTN_ID,
            text=Const(kb_texts.LOCATION),
            state=ProfileEditStates.location,
            data=DATA
        ),
        width=2
    ),
    get_back_button(state=ProfileStates.info),
    getter=data_getter,
    state=ProfileStates.edit_field
)
