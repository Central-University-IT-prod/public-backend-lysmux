from . import (
    users,
    travels,
    locations,
    notes
)

routers = (
    users.router,
    travels.router,
    locations.router,
    notes.router
)
