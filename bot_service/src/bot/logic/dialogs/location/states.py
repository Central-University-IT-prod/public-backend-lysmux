from aiogram.fsm.state import StatesGroup, State


class LocationStates(StatesGroup):
    list = State()
    info = State()
    confirm_delete = State()
    edit_field = State()
