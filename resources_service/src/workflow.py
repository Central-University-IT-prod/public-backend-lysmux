from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import AsyncContextManager, Callable

from frousquare_api import FourSquareAPI
from kupibilet_api import KupiBiletAPI
from nominatim_api.api import NominatimAPI
from openmeteo_api import OpenMeteoAPI
from route_service import RouteService
from rzd_api import RzdAPI
from settings import Settings


@dataclass
class WorkflowData:
    nominatim_api: NominatimAPI
    open_meteo_api: OpenMeteoAPI
    foursquare_api: FourSquareAPI
    rzd_api: RzdAPI
    kupibilet_api: KupiBiletAPI
    route_service: RouteService


def workflow_manager(settings: Settings):
    @asynccontextmanager
    async def _inner():
        nominatim_api = NominatimAPI()
        open_meteo_api = OpenMeteoAPI()
        foursquare_api = FourSquareAPI(
            api_key=settings.foursquare_key
        )
        rzd_api = RzdAPI()
        kupibilet_api = KupiBiletAPI()
        route_service = RouteService()

        yield WorkflowData(
            nominatim_api=nominatim_api,
            open_meteo_api=open_meteo_api,
            foursquare_api=foursquare_api,
            rzd_api=rzd_api,
            route_service=route_service,
            kupibilet_api=kupibilet_api
        )

        await nominatim_api.close()
        await open_meteo_api.close()
        await foursquare_api.close()
        await rzd_api.close()
        await kupibilet_api.close()
        await route_service.close()

    return _inner


WorkflowManager = Callable[
    [], AsyncContextManager[WorkflowData]
]
