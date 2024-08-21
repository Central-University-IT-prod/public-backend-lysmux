from aiogram import Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.api.exceptions import UnknownIntent, UnknownState

from bot.logic.dialogs.general.states import GeneralStates

router = Router()


@router.error(ExceptionTypeFilter(UnknownState, UnknownIntent))
async def dialog_error_handler(
        event: ErrorEvent,
        dialog_manager: DialogManager
) -> None:
    """
    Handle dialog error. Switch to menu
    """
    await dialog_manager.start(
        state=GeneralStates.menu,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND
    )
