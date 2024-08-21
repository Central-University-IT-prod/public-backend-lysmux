from aiogram.fsm.state import StatesGroup, State


class GuideStates(StatesGroup):
    action = State()

    weather = State()
    attractions = State()
    caterings_location = State()
    caterings = State()
    hotels = State()

    tickets_type = State()
    tickets_from = State()
    air_tickets = State()
    train_tickets = State()

    route_from = State()
    route = State()
