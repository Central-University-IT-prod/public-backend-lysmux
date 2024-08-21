from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.logic.dialogs.profile.states import ProfileStates
from bot.middlewares import is_user_registered

router = Router()
router.message.middleware(is_user_registered)
router.callback_query.middleware(is_user_registered)


@router.message(Command("profile"))
async def profile(
        message: Message,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(
        state=ProfileStates.info,
        mode=StartMode.RESET_STACK
    )
