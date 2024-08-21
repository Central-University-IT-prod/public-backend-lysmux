from aiogram.fsm.state import StatesGroup, State


class LocationEditStates(StatesGroup):
    name = State()
    location = State()
    start_date = State()
    end_date = State()
