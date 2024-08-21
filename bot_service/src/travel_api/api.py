from httpx import AsyncClient
from pydantic import TypeAdapter

from .schemas.location import (
    TravelLocation,
    TravelLocationUpdate,
    TravelLocationCreate
)
from .schemas.note import Note, NoteCreate, NoteUpdate
from .schemas.travel import Travel, TravelUpdate, TravelCreate
from .schemas.user import User, UserUpdate


class TravelApi:
    def __init__(
            self,
            host: str,
            port: int
    ) -> None:
        self._http_client = AsyncClient(
            follow_redirects=True,
            base_url=f"http://{host}:{port}"
        )

    async def get_user(self, user_id: int) -> User | None:
        response = await self._http_client.get(
            url=f"/users/{user_id}"
        )
        if response.status_code != 200:
            return None
        return User.model_validate(response.json())

    async def create_user(self, user: User) -> None:
        await self._http_client.post(
            url="/users/create",
            json=user.model_dump()
        )

    async def update_user(
            self,
            user_id: int,
            update_schema: UserUpdate
    ) -> None:
        await self._http_client.patch(
            url=f"/users/{user_id}",
            json=update_schema.model_dump(exclude_none=True)
        )

    async def get_user_travels(
            self,
            user_id: int
    ) -> list[Travel]:
        response = await self._http_client.get(
            url=f"/travels/user/{user_id}"
        )
        adapter = TypeAdapter(list[Travel])
        return adapter.validate_python(response.json())

    async def get_travel(self, travel_id: str) -> Travel | None:
        response = await self._http_client.get(
            url=f"/travels/{travel_id}"
        )
        if response.status_code != 200:
            return None
        return Travel.model_validate(response.json())

    async def add_travel(
            self,
            create_schema: TravelCreate
    ) -> None:
        await self._http_client.post(
            url="/travels/create",
            json=create_schema.model_dump()
        )

    async def update_travel(
            self,
            travel_id: str,
            update_schema: TravelUpdate
    ) -> None:
        await self._http_client.patch(
            url=f"/travels/{travel_id}",
            json=update_schema.model_dump(exclude_none=True, mode="json")
        )

    async def get_travel_locations(
            self,
            travel_id: str
    ) -> list[TravelLocation]:
        response = await self._http_client.get(
            url=f"/locations/travel/{travel_id}"
        )
        adapter = TypeAdapter(list[TravelLocation])
        return adapter.validate_python(response.json())

    async def get_travel_location(
            self,
            location_id: str
    ) -> TravelLocation | None:
        response = await self._http_client.get(
            url=f"/locations/{location_id}"
        )
        if response.status_code != 200:
            return None
        return TravelLocation.model_validate(response.json())

    async def delete_travel(self, travel_id: str) -> None:
        await self._http_client.delete(
            url=f"/travels/{travel_id}"
        )

    async def add_travel_location(
            self,
            create_schema: TravelLocationCreate
    ) -> None:
        await self._http_client.post(
            url="/locations/add",
            json=create_schema.model_dump(mode="json")
        )

    async def update_travel_location(
            self,
            location_id: str,
            update_schema: TravelLocationUpdate
    ) -> None:
        await self._http_client.patch(
            url=f"/locations/{location_id}",
            json=update_schema.model_dump(exclude_none=True, mode="json")
        )

    async def delete_travel_location(self, location_id: str) -> None:
        await self._http_client.delete(
            url=f"/locations/{location_id}"
        )

    async def delete_travel_participant(
            self,
            travel_id: str,
            user_id: int
    ) -> None:
        await self._http_client.delete(
            url=f"/travels/{travel_id}/participant/{user_id}"
        )

    async def add_travel_participant(
            self,
            travel_id: str,
            user_id: int
    ) -> None:
        await self._http_client.post(
            url=f"/travels/{travel_id}/participant/{user_id}"
        )

    async def get_notes(self, travel_id: str) -> list[Note]:
        response = await self._http_client.get(
            url=f"/notes/travel/{travel_id}"
        )
        adapter = TypeAdapter(list[Note])
        return adapter.validate_python(response.json())

    async def get_note(self, note_id: str) -> Note | None:
        response = await self._http_client.get(
            url=f"/notes/{note_id}"
        )
        if response.status_code != 200:
            return None
        return Note.model_validate(response.json())

    async def add_note(
            self,
            create_schema: NoteCreate
    ) -> None:
        await self._http_client.post(
            url="/notes/add",
            json=create_schema.model_dump(mode="json")
        )

    async def update_note(
            self,
            note_id: str,
            update_schema: NoteUpdate
    ) -> None:
        await self._http_client.patch(
            url=f"/notes/{note_id}",
            json=update_schema.model_dump(exclude_none=True, mode="json")
        )

    async def delete_note(self, note_id: str) -> None:
        await self._http_client.delete(
            url=f"/notes/{note_id}"
        )

    async def __aenter__(self) -> "TravelApi":
        return self

    async def close(self) -> None:
        await self._http_client.aclose()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
