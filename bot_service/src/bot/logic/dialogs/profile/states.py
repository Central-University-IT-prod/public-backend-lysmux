from aiogram.fsm.state import StatesGroup, State


class ProfileStates(StatesGroup):
    info = State()
    edit_field = State()
