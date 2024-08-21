from httpx import AsyncClient


class ApiClient:
    def __init__(
            self,
            host: str,
            port: int
    ) -> None:
        self._http_client = AsyncClient(
            follow_redirects=True,
            base_url=f"http://{host}:{port}"
        )

    async def __aenter__(self) -> "ApiClient":
        return self

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
