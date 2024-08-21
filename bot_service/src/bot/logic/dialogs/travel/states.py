from aiogram.fsm.state import StatesGroup, State


class TravelStates(StatesGroup):
    list = State()
    info = State()
    confirm_delete = State()
    edit_field = State()
