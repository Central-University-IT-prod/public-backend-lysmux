from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.participant.states import ParticipantStates
from bot.multimedia.inline_texts import location as inline_texts
from travel_api import TravelApi


async def on_participant_delete(
        event: CallbackQuery,
        select: Button,
        dialog_manager: DialogManager,
) -> None:
    travel_api: TravelApi = dialog_manager.middleware_data["travel_api"]
    travel_id: str = dialog_manager.start_data["travel_id"]
    participant_id: int = dialog_manager.dialog_data["sel_participant_id"]

    await travel_api.delete_travel_participant(
        travel_id=travel_id,
        user_id=participant_id
    )
    await event.answer(inline_texts.DELETED)
    await dialog_manager.switch_to(
        state=ParticipantStates.list
    )
