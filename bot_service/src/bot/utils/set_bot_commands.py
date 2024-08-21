from aiogram import Bot
from aiogram.types import BotCommand

commands = {
    "start": "Главное меню",
    "travels": "Мои путешествия",
    "profile": "Мой профиль",
}


async def set_bot_commands(bot: Bot) -> None:
    await bot.set_my_commands(commands=[
        BotCommand(command=command, description=description)
        for command, description in commands.items()
    ])
