from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select

from bot.logic.dialogs.participant.states import ParticipantStates


async def on_participant_select(
        event: CallbackQuery,
        select: Select,
        dialog_manager: DialogManager,
        participant_id: str,
) -> None:
    dialog_manager.dialog_data["sel_participant_id"] = participant_id

    await dialog_manager.switch_to(
        state=ParticipantStates.info
    )
