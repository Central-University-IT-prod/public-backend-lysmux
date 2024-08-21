from aiogram.fsm.state import StatesGroup, State


class NoteEditStates(StatesGroup):
    content = State()
    name = State()
    scope = State()
