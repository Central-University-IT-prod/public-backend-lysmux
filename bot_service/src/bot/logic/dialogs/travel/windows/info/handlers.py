from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.location.states import LocationStates
from bot.logic.dialogs.note.states import NoteState
from bot.logic.dialogs.participant.states import ParticipantStates


async def show_notes(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
) -> None:
    travel_id: str = dialog_manager.dialog_data["sel_travel_id"]
    await dialog_manager.start(
        state=NoteState.list,
        data={
            "travel_id": travel_id
        }
    )


async def show_locations(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
) -> None:
    travel_id: str = dialog_manager.dialog_data["sel_travel_id"]
    await dialog_manager.start(
        state=LocationStates.list,
        data={
            "travel_id": travel_id
        }
    )


async def show_participants(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
) -> None:
    travel_id: str = dialog_manager.dialog_data["sel_travel_id"]
    await dialog_manager.start(
        state=ParticipantStates.list,
        data={
            "travel_id": travel_id
        }
    )
