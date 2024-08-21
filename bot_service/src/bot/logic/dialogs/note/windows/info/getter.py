from typing import Any

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId

from travel_api import TravelApi


async def data_getter(
        travel_api: TravelApi,
        dialog_manager: DialogManager,
        **kwargs
) -> dict[str, Any]:
    note_id: str = dialog_manager.dialog_data["sel_note_id"]
    note = await travel_api.get_note(note_id)

    if note.file_id:
        media = MediaAttachment(
            type=ContentType(note.content_type),
            file_id=MediaId(file_id=note.file_id)
        )
    else:
        media = None

    return {
        "note": note,
        "media": media
    }
