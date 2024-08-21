from aiogram.fsm.state import StatesGroup, State


class TravelEditStates(StatesGroup):
    name = State()
    description = State()
