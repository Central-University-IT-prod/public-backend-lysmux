from . import (
    general,
    travel,
    travel_edit,
    note,
    note_edit,
    guide,
    profile,
    profile_edit,
    location,
    location_edit,
    participant
)

routers = (
    general.dialog,
    travel.dialog,
    travel_edit.dialog,
    note.dialog,
    note_edit.dialog,
    guide.dialog,
    profile.dialog,
    profile_edit.dialog,
    location.dialog,
    location_edit.dialog,
    participant.dialog
)
