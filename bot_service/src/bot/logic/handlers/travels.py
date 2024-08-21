from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.logic.dialogs.travel.states import TravelStates
from bot.middlewares import is_user_registered

router = Router()
router.message.middleware(is_user_registered)
router.callback_query.middleware(is_user_registered)


@router.message(Command("travels"))
async def list_travels(
        message: Message,
        dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(
        state=TravelStates.list,
        mode=StartMode.RESET_STACK
    )
