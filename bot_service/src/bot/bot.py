from datetime import timedelta

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import (
    RedisStorage,
    RedisEventIsolation,
    DefaultKeyBuilder
)
from redis.asyncio import Redis

from bot.logic import handlers, dialogs, errors
from bot.middlewares import UserMiddleware
from settings import RedisSettings, Settings


def get_storage(settings: RedisSettings) -> RedisStorage:
    ttl = timedelta(weeks=1)
    redis = Redis(
        host=settings.host,
        port=settings.port,
        password=settings.password
    )
    storage = RedisStorage(
        redis,
        key_builder=DefaultKeyBuilder(with_destiny=True),
        data_ttl=ttl,
        state_ttl=ttl
    )

    return storage


def get_dispatcher(settings: Settings) -> Dispatcher:
    storage = get_storage(settings.redis)
    dispatcher = Dispatcher(
        storage=storage,
        events_isolation=RedisEventIsolation(storage.redis)
    )

    dispatcher.include_routers(
        *errors.routers,
        *handlers.routers,
        *dialogs.routers,
    )

    for mid in (
            UserMiddleware(),
    ):
        dispatcher.message.middleware(mid)
        dispatcher.callback_query.middleware(mid)

    return dispatcher


def get_bot(token: str) -> Bot:
    bot = Bot(
        token=token,
        parse_mode=ParseMode.HTML
    )
    return bot
