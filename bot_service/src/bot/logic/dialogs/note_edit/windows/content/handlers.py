from typing import Any

from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram_dialog import DialogManager

from bot.logic.dialogs.note_edit.states import NoteEditStates
from bot.utils.ce_handler import CEHandler


def get_file_id(event: Message) -> str | None:
    match event.content_type:
        case ContentType.PHOTO:
            return event.photo[-1].file_id
        case ContentType.VIDEO:
            return event.video.file_id
        case ContentType.DOCUMENT:
            return event.document.file_id


class ContentHandler(CEHandler):
    async def process_create(
            self,
            event: Message,
            manager: DialogManager,
            source: Any,
            data: Any
    ) -> None:
        manager.dialog_data["content_type"] = event.content_type
        manager.dialog_data["text"] = event.text or event.caption
        manager.dialog_data["file_id"] = get_file_id(event)

        await manager.switch_to(
            state=NoteEditStates.name
        )

    async def process_edit(
            self,
            event: Message,
            manager: DialogManager,
            source: Any,
            data: Any
    ) -> None:
        await manager.done(
            {
                "action": "edit",
                "content_type": event.content_type,
                "text": event.text or event.caption
            }
        )
