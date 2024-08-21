from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery

from travel_api import TravelApi


class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[
                [TelegramObject, dict[str, Any]],
                Awaitable[Any]
            ],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        if isinstance(event, Message | CallbackQuery):
            travel_api: TravelApi = data["travel_api"]
            user = await travel_api.get_user(event.from_user.id)  # type: ignore
            data["user"] = user

        return await handler(event, data)
