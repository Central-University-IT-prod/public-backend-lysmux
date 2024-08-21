from datetime import date

from pydantic import TypeAdapter

from resources_api.base_api import ApiClient
from .schemas import Forecast


class ForecastAPI(ApiClient):
    async def forecast(
            self,
            latitude: float,
            longitude: float,
            start_date: date,
            end_date: date
    ) -> list[Forecast]:
        response = await self._http_client.get(
            url="/forecast?",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
            }
        )
        if response.status_code != 200:
            return []
        adapter = TypeAdapter(list[Forecast])
        return adapter.validate_python(response.json())
