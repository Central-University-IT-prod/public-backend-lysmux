from contextlib import asynccontextmanager

from fastapi import FastAPI

from .endpoints import routers
from workflow import WorkflowManager


def lifespan(workflow_manager: WorkflowManager):
    @asynccontextmanager
    async def _inner(app: FastAPI):
        async with workflow_manager() as workflow_data:
            yield {
                "workflow_data": workflow_data
            }

    return _inner


def get_app(workflow_manager: WorkflowManager) -> FastAPI:
    app = FastAPI(
        lifespan=lifespan(workflow_manager)
    )

    for router in routers:
        app.include_router(router)

    return app
