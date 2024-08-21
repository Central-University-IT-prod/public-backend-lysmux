from aiogram import Bot


async def notify_users(
        bot: Bot,
        users: list[int],
        message: str
) -> None:
    for user_id in users:
        await bot.send_message(chat_id=user_id, text=message)