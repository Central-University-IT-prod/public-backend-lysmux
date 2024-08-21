from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.note_edit.states import NoteEditStates


async def on_edit_name(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    note_id: str = manager.dialog_data["sel_note_id"]
    await manager.start(
        state=NoteEditStates.name,
        data={
            "edit": True,
            "note_id": note_id
        }
    )


async def on_edit_content(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    note_id: str = manager.dialog_data["sel_note_id"]
    await manager.start(
        state=NoteEditStates.content,
        data={
            "edit": True,
            "note_id": note_id
        }
    )


async def on_edit_scope(
        event: CallbackQuery,
        button: Button,
        manager: DialogManager,
) -> None:
    note_id: str = manager.dialog_data["sel_note_id"]
    await manager.start(
        state=NoteEditStates.scope,
        data={
            "edit": True,
            "note_id": note_id
        }
    )
