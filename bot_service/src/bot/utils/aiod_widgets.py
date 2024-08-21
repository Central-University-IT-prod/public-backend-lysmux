from typing import Dict

from aiogram.types import (
    InlineKeyboardButton,
    KeyboardButton,
    KeyboardButtonRequestUsers
)
from aiogram_dialog import DialogManager
from aiogram_dialog.api.internal import RawKeyboard
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.kbd import Keyboard
from aiogram_dialog.widgets.text import Text


class SwitchInlineCurChatQuery(Keyboard):
    def __init__(
            self,
            text: Text,
            switch_inline_query: Text,
            id: str | None = None,
            when: WhenCondition = None,
    ) -> None:
        super().__init__(id=id, when=when)
        self.text = text
        self.switch_inline = switch_inline_query

    async def _render_keyboard(
            self,
            data: Dict,
            manager: DialogManager,
    ) -> RawKeyboard:
        text = await self.text.render_text(data, manager)
        query = await self.switch_inline.render_text(data, manager)
        return [
            [
                InlineKeyboardButton(
                    text=text,
                    switch_inline_query_current_chat=query,
                ),
            ],
        ]


class RequestUser(Keyboard):
    def __init__(
            self,
            text: Text,
            request_id: int,
            user_is_bot: bool | None = None,
            user_is_premium: bool | None = None,
            max_quantity: int | None = None,
            when: WhenCondition = None,
    ) -> None:
        super().__init__(when=when)
        self.text = text
        self.request_id = request_id
        self.user_is_bot = user_is_bot
        self.user_is_premium = user_is_premium
        self.max_quantity = max_quantity

    async def _render_keyboard(
            self,
            data: dict,
            manager: DialogManager,
    ) -> RawKeyboard:
        return [
            [
                KeyboardButton(
                    request_users=KeyboardButtonRequestUsers(
                        request_id=self.request_id,
                        user_is_bot=self.user_is_bot,
                        user_is_premium=self.user_is_premium,
                        max_quantity=self.max_quantity
                    ),
                    text=await self.text.render_text(data, manager)
                )
            ],
        ]
