from . import (
    location,
    route,
    forecast,
    places,
    train_tickets,
    air_tickets
)

routers = (
    location.router,
    route.router,
    forecast.router,
    places.router,
    train_tickets.router,
    air_tickets.router
)
