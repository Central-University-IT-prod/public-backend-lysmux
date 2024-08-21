import asyncio

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from bot.logic.dialogs.participant.states import ParticipantStates
from bot.utils.notifier import notify_users
from bot.utils.template_engine import render_template
from travel_api import TravelApi


async def on_participant(
        event: Message,
        source: MessageInput,
        manager: DialogManager,
) -> None:
    travel_api: TravelApi = manager.middleware_data["travel_api"]
    travel_id: str = manager.start_data["travel_id"]
    travel = await travel_api.get_travel(travel_id)
    user_id = event.users_shared.user_ids[0]

    if user_id == event.from_user.id:
        await event.answer(
            text=render_template("participants/errors/can_not_add_self.html")
        )
        return

    user = await travel_api.get_user(user_id)
    if user is None:
        await event.answer(
            text=render_template("participants/errors/user_not_found.html")
        )
        return

    await travel_api.add_travel_participant(
        travel_id=travel_id,
        user_id=user_id
    )

    await event.bot.send_message(chat_id=user_id, text=render_template(
        name="notification/you_are_invited.html",
        travel_name=travel.name,
    ))

    loop = asyncio.get_running_loop()
    await loop.create_task(notify_users(
        bot=event.bot,
        users=[
            p.id
            for p in travel.participants
        ],
        message=render_template(
            name="notification/new_participant.html",
            travel_name=travel.name,
            member=user.name
        )
    ))
    await manager.switch_to(state=ParticipantStates.list)
