from aiogram_dialog import Dialog, DialogManager

from bot.middlewares import is_user_registered
from .states import NoteState
from .windows import windows


async def on_result(
        start_data: dict,
        result: dict,
        manager: DialogManager
) -> None:
    if not result:
        return

    match result.get("action"):
        case "create":
            await manager.switch_to(
                state=NoteState.list
            )
        case "edit":
            await manager.switch_to(
                state=NoteState.info
            )


dialog = Dialog(*windows, on_process_result=on_result)
dialog.message.middleware(is_user_registered)
dialog.callback_query.middleware(is_user_registered)
