from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import AsyncContextManager, Callable

from sqlalchemy.ext.asyncio import async_sessionmaker

from core.database import get_session_maker
from settings import Settings


@dataclass
class WorkflowData:
    session_maker: async_sessionmaker


def workflow_manager(settings: Settings):
    @asynccontextmanager
    async def _inner():
        session_maker = get_session_maker(database_url=settings.database_url)

        yield WorkflowData(
            session_maker=session_maker
        )

    return _inner


WorkflowManager = Callable[
    [], AsyncContextManager[WorkflowData]
]
