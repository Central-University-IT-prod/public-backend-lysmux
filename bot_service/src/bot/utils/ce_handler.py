from abc import ABC, abstractmethod
from typing import Any

from aiogram_dialog import DialogManager, ChatEvent


class CEHandler(ABC):
    async def __call__(
            self,
            event: ChatEvent,
            source: Any,
            manager: DialogManager,
            data: Any = None
    ) -> None:
        start_data = manager.start_data or {}

        if not await self.validate(
                event=event,
                manager=manager,
                source=source,
                data=data
        ):
            await self.on_validation_error(
                event=event,
                manager=manager,
                source=source,
                data=data
            )
            return

        if start_data.get("edit"):
            await self.process_edit(
                event=event,
                manager=manager,
                source=source,
                data=data
            )
        else:
            await self.process_create(
                event=event,
                manager=manager,
                source=source,
                data=data
            )

    async def validate(
            self,
            event: ChatEvent,
            manager: DialogManager,
            source: Any,
            data: Any
    ) -> bool:
        return True

    async def on_validation_error(
            self,
            event: ChatEvent,
            manager: DialogManager,
            source: Any,
            data: Any
    ) -> None:
        pass

    @abstractmethod
    async def process_create(
            self,
            event: ChatEvent,
            manager: DialogManager,
            source: Any,
            data: Any
    ) -> None:
        pass

    @abstractmethod
    async def process_edit(
            self,
            event: ChatEvent,
            manager: DialogManager,
            source: Any,
            data: Any
    ) -> None:
        pass
