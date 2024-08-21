from aiogram.fsm.state import StatesGroup, State


class NoteState(StatesGroup):
    info = State()
    list = State()
    confirm_delete = State()
    edit_field = State()
