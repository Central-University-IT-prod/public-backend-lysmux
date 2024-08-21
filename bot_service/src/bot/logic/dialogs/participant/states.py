from aiogram.fsm.state import StatesGroup, State


class ParticipantStates(StatesGroup):
    list = State()
    info = State()
    add = State()
    confirm_delete = State()
