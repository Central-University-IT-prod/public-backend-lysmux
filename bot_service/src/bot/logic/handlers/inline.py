from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultLocation

from resources_api import APIGateway

router = Router()


@router.inline_query()
async def inline_location(
        inline_query: InlineQuery,
        api_gateway: APIGateway
) -> None:
    locations = await api_gateway.location_api.suggest(
        query=inline_query.query
    )

    await inline_query.answer(
        results=[
            InlineQueryResultLocation(
                id=str(location.osm_id),
                latitude=location.latitude,
                longitude=location.longitude,
                title=location.display_name
            )
            for location in locations
        ]
    )
