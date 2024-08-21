from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.logic.dialogs.general.states import GeneralStates
from bot.middlewares import is_user_registered

router = Router()
router.message.middleware(is_user_registered)
router.callback_query.middleware(is_user_registered)


@router.message(CommandStart())
async def start_handler(
        message: Message,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(
        GeneralStates.menu,
        mode=StartMode.RESET_STACK
    )
