from typing import Any

from aiogram_dialog import Dialog, DialogManager, Data

from bot.middlewares import is_user_registered
from .states import TravelStates
from .windows import windows


async def on_result(
        start_data: Data,
        result: dict[str, Any] | None,
        manager: DialogManager
) -> None:
    if not result:
        return

    match result.get("action"):
        case "create":
            await manager.switch_to(
                state=TravelStates.list
            )
        case "edit":
            await manager.switch_to(
                state=TravelStates.info
            )


dialog = Dialog(*windows, on_process_result=on_result)
dialog.message.middleware(is_user_registered)
dialog.callback_query.middleware(is_user_registered)
