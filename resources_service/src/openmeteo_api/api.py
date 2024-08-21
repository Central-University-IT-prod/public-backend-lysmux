from datetime import date

import httpx
from cashews import cache, noself

from .schemas import Forecast

TEMP_MAX = "temperature_2m_max"
TEMP_MIN = "temperature_2m_min"
APPARENT_TEMP_MIN = "apparent_temperature_min"
APPARENT_TEMP_MAX = "apparent_temperature_max"
PRECIPITATION_PROB = "precipitation_probability_max"
WIND_SPEED = "wind_speed_10m_max"
WIND_DIRECTION = "wind_direction_10m_dominant"

FORECAST_VARS = (
    TEMP_MAX,
    TEMP_MIN,
    APPARENT_TEMP_MIN,
    APPARENT_TEMP_MAX,
    PRECIPITATION_PROB,
    WIND_SPEED,
    WIND_DIRECTION
)


class OpenMeteoAPI:
    def __init__(self) -> None:
        self._http_client = httpx.AsyncClient(
            base_url="https://api.open-meteo.com/v1"
        )

    @noself(cache)(ttl="1h")
    async def get_forecast(
            self,
            latitude: float,
            longitude: float,
            start_date: date,
            end_date: date
    ) -> list[Forecast]:
        forecasts = []
        response = await self._http_client.get(
            url="/forecast?",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                "wind_speed_unit": "ms",
                "daily": ",".join(FORECAST_VARS)
            }
        )
        data = response.json()
        if data.get("error"):
            return []

        daily = response.json()["daily"]
        for idx in range(len(daily["time"])):
            forecasts.append(
                Forecast(
                    date=daily["time"][idx],
                    temperature_min=daily[TEMP_MIN][idx],
                    temperature_max=daily[TEMP_MAX][idx],
                    temperature_apparent_min=daily[APPARENT_TEMP_MIN][idx],
                    temperature_apparent_max=daily[APPARENT_TEMP_MAX][idx],
                    precipitation_probability=daily[PRECIPITATION_PROB][idx],
                    wind_speed=daily[WIND_SPEED][idx],
                    wind_direction=daily[WIND_DIRECTION][idx],
                )
            )

        return forecasts

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aenter__(self) -> "OpenMeteoAPI":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
