from contextlib import asynccontextmanager
from typing import TypedDict, AsyncGenerator

from resources_api import APIGateway
from settings import Settings
from travel_api.api import TravelApi


class WorkflowData(TypedDict):
    api_gateway: APIGateway
    travel_api: TravelApi


@asynccontextmanager
async def workflow_manager(
        settings: Settings
) -> AsyncGenerator[WorkflowData, None]:
    api_gateway = APIGateway(
        host=settings.resources_service_host,
        port=settings.resources_service_port
    )
    travel_api = TravelApi(
        host=settings.travel_service_host,
        port=settings.travel_service_port
    )

    yield WorkflowData(
        api_gateway=api_gateway,
        travel_api=travel_api
    )

    await api_gateway.close()
    await travel_api.close()
