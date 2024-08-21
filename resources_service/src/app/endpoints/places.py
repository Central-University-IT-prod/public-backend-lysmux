from typing import Annotated

from fastapi import APIRouter, Query

from app.dependencies import FourSquareAPIDep
from frousquare_api.schemas import Place

router = APIRouter(
    prefix="/places",
    tags=["Places"]
)


@router.get(
    path="/suggest_attractions",
    response_model=list[Place]
)
async def suggest_attractions(
        foursquare_api: FourSquareAPIDep,
        longitude_min: Annotated[float, Query(
            ge=-180,
            le=180
        )],
        longitude_max: Annotated[float, Query(
            ge=-180,
            le=180
        )],
        latitude_min: Annotated[float, Query(
            ge=-90,
            le=90
        )],
        latitude_max: Annotated[float, Query(
            ge=-90,
            le=90
        )],
        limit: Annotated[int, Query(ge=1, le=100)] = 20
) -> list[Place]:
    places = await foursquare_api.suggest_attractions(
        longitude_min=longitude_min,
        longitude_max=longitude_max,
        latitude_min=latitude_min,
        latitude_max=latitude_max,
        limit=limit
    )
    return places


@router.get(
    path="/suggest_hotels",
    response_model=list[Place]
)
async def suggest_hotels(
        foursquare_api: FourSquareAPIDep,
        longitude_min: Annotated[float, Query(
            ge=-180,
            le=180
        )],
        longitude_max: Annotated[float, Query(
            ge=-180,
            le=180
        )],
        latitude_min: Annotated[float, Query(
            ge=-90,
            le=90
        )],
        latitude_max: Annotated[float, Query(
            ge=-90,
            le=90
        )],
        limit: Annotated[int, Query(ge=1, le=100)] = 20
) -> list[Place]:
    hotels = await foursquare_api.suggest_hotels(
        longitude_min=longitude_min,
        longitude_max=longitude_max,
        latitude_min=latitude_min,
        latitude_max=latitude_max,
        limit=limit
    )
    return hotels


@router.get(
    "/suggest_caterings",
    response_model=list[Place]
)
async def suggest_caterings(
        foursquare_api: FourSquareAPIDep,
        longitude: Annotated[float, Query(
            ge=-180,
            le=180
        )],
        latitude: Annotated[float, Query(
            ge=-90,
            le=90
        )],
        radius: Annotated[int, Query(ge=1, le=100000)] = 1000,
        limit: Annotated[int, Query(ge=1, le=100)] = 20
) -> list[Place]:
    places = await foursquare_api.suggest_caterings(
        longitude=longitude,
        latitude=latitude,
        radius=radius,
        limit=limit
    )
    return places
