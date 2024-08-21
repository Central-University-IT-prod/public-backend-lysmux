from aiogram.fsm.state import StatesGroup, State


class ProfileEditStates(StatesGroup):
    name = State()
    age = State()
    bio = State()
    location = State()
