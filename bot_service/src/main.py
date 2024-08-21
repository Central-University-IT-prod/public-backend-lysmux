import asyncio
import locale
import logging

from aiogram_dialog import setup_dialogs
from aiogram_dialog.widgets.text.jinja import JINJA_ENV_FIELD

from bot.bot import get_dispatcher, get_bot
from bot.utils.aiod_managers import CustomMessageManager
from bot.utils.set_bot_commands import set_bot_commands
from bot.utils.template_engine import jinja_env
from settings import Settings
from workflow import workflow_manager

locale.setlocale(locale.LC_ALL, "ru-RU")

logger = logging.getLogger(__name__)


async def run_bot(settings: Settings) -> None:
    dispatcher = get_dispatcher(settings=settings)
    bot = get_bot(token=settings.bot_token)

    await set_bot_commands(bot)

    # setup aiogram dialogs
    setup_dialogs(dispatcher, message_manager=CustomMessageManager())
    setattr(bot, JINJA_ENV_FIELD, jinja_env)  # for aio dialogs

    await bot.delete_webhook(drop_pending_updates=True)

    async with workflow_manager(settings) as workflow_data:
        dispatcher.workflow_data = workflow_data  # type: ignore
        await dispatcher.start_polling(bot)


def main() -> None:
    settings = Settings()  # type: ignore[reportCallIssue]
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    try:
        logger.info("GorZdrav bot is running")
        asyncio.run(run_bot(settings=settings))
    except (KeyboardInterrupt, SystemExit):
        logger.info("GorZdrav bot stopped")


if __name__ == '__main__':
    main()
