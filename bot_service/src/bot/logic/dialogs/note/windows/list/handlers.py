from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select, Button

from bot.logic.dialogs.note.states import NoteState
from bot.logic.dialogs.note_edit.states import NoteEditStates


async def on_note_select(
        event: CallbackQuery,
        select: Select,
        dialog_manager: DialogManager,
        note_id: str,
) -> None:
    dialog_manager.dialog_data["sel_note_id"] = note_id
    await dialog_manager.switch_to(
        state=NoteState.info
    )


async def on_note_add(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager,
) -> None:
    travel_id: str = dialog_manager.start_data["travel_id"]

    await dialog_manager.start(
        state=NoteEditStates.content,
        data={
            "travel_id": travel_id
        }
    )
