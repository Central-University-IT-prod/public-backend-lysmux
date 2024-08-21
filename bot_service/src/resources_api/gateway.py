from resources_api.air_tickets import AirTicketsAPI
from resources_api.forecast import ForecastAPI
from resources_api.location import LocationAPI
from resources_api.places import PlacesAPI
from resources_api.route import RouteAPI
from resources_api.train_tickets.api import TrainTicketsAPI


class APIGateway:
    def __init__(
            self,
            host: str,
            port: int
    ) -> None:
        self.air_tickets_api = AirTicketsAPI(host=host, port=port)
        self.forecast_api = ForecastAPI(host=host, port=port)
        self.location_api = LocationAPI(host=host, port=port)
        self.places_api = PlacesAPI(host=host, port=port)
        self.train_tickets_api = TrainTicketsAPI(host=host, port=port)
        self.route_api = RouteAPI(host=host, port=port)

    async def __aenter__(self) -> "APIGateway":
        return self

    async def close(self) -> None:
        await self.air_tickets_api.close()
        await self.forecast_api.close()
        await self.location_api.close()
        await self.places_api.close()
        await self.train_tickets_api.close()
        await self.route_api.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
