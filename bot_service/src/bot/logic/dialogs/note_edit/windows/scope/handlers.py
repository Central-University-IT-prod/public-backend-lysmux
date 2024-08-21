from typing import Any

from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Button

from bot.utils.ce_handler import CEHandler
from .ids import PUBLIC_SCOPE_BTN_ID


class ScopeHandler(CEHandler):
    async def process_create(
            self,
            event: ChatEvent,
            manager: DialogManager,
            source: Button,
            data: Any
    ) -> None:
        name: str = manager.dialog_data["name"]
        file_id: str = manager.dialog_data.get("file_id")
        content_type: str = manager.dialog_data.get("content_type")
        text: str = manager.dialog_data.get("text")

        await manager.done(
            {
                "action": "create",
                "name": name,
                "file_id": file_id,
                "content_type": content_type,
                "text": text,
                "is_public": source.widget_id == PUBLIC_SCOPE_BTN_ID
            }
        )

    async def process_edit(
            self,
            event: ChatEvent,
            manager: DialogManager,
            source: Button,
            data: Any
    ) -> None:
        await manager.done(
            {
                "action": "edit",
                "is_public": source.widget_id == PUBLIC_SCOPE_BTN_ID
            }
        )
