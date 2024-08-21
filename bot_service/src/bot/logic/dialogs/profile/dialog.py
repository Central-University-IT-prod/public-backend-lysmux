from aiogram_dialog import Dialog, DialogManager

from .states import ProfileStates
from .windows import windows


async def on_result(
        start_data: dict,
        result: str,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.switch_to(
        state=ProfileStates.info
    )


dialog = Dialog(*windows, on_process_result=on_result)
