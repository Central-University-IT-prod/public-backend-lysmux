from datetime import date
from typing import Annotated

from fastapi import APIRouter, Query

from app.dependencies import OpenMeteoAPIDep
from openmeteo_api.schemas import Forecast

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)


@router.get(
    path="",
    response_model=list[Forecast]
)
async def get_forecast(
        latitude: Annotated[float, Query(
            ge=-90,
            le=90
        )],
        longitude: Annotated[float, Query(
            ge=-180,
            le=180
        )],
        start_date: Annotated[date, Query()],
        end_date: Annotated[date, Query()],
        open_meteo_api: OpenMeteoAPIDep
) -> list[Forecast]:
    return await open_meteo_api.get_forecast(
        latitude=latitude,
        longitude=longitude,
        start_date=start_date,
        end_date=end_date
    )
