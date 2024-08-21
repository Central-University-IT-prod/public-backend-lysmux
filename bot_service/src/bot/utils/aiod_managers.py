from aiogram import Bot
from aiogram.types import InputFile, BufferedInputFile
from aiogram_dialog.api.entities import MediaAttachment
from aiogram_dialog.manager.message_manager import MessageManager


class CustomMessageManager(MessageManager):
    async def get_media_source(
            self, media: MediaAttachment, bot: Bot,
    ) -> InputFile | str:
        if media.file_id:
            return await super().get_media_source(media, bot)
        if isinstance(media.url, bytes):
            return BufferedInputFile(media.url, f"image.png")
        return await super().get_media_source(media, bot)
