from aiogram.types import CallbackQuery, User
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.logic.dialogs.guide.states import GuideStates
from travel_api import TravelApi


async def show_guide(
        event: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
) -> None:
    travel_api: TravelApi = dialog_manager.middleware_data["travel_api"]
    travel_id: str = dialog_manager.start_data["travel_id"]
    participant_id: int = dialog_manager.dialog_data["sel_participant_id"]
    event_from_user: User = dialog_manager.middleware_data["event_from_user"]
    participant = await travel_api.get_user(participant_id)
    travel = await travel_api.get_travel(travel_id)
    user_is_owner = travel.owner.id == event_from_user.id

    await dialog_manager.start(
        state=GuideStates.action,
        data={
            "participant": participant,
            "owner_id": travel.owner.id,
            "user_is_owner": user_is_owner
        }
    )
