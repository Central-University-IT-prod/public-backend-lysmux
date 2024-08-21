from io import BytesIO
from typing import Annotated

from fastapi import APIRouter, Query
from starlette.responses import Response

from app.dependencies import RouteServiceDep
from app.errors import ROUTE_NOT_FOUND

router = APIRouter(
    prefix="/route",
    tags=["Route"]
)


@router.get(
    path="",
    response_class=Response
)
async def build_route(
        route_service: RouteServiceDep,
        from_latitude: Annotated[float, Query()],
        from_longitude: Annotated[float, Query()],
        to_latitude: Annotated[float, Query()],
        to_longitude: Annotated[float, Query()],
) -> Response:
    route_img = await route_service.build_route(
        from_latitude=from_latitude,
        from_longitude=from_longitude,
        to_latitude=to_latitude,
        to_longitude=to_longitude
    )
    if route_img is None:
        raise ROUTE_NOT_FOUND

    img_io = BytesIO()
    route_img.save(img_io, "png")
    return Response(
        content=img_io.getvalue(),
        media_type="image/png"
    )
