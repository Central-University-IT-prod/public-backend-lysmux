from fastapi import HTTPException
from starlette import status

NOTE_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Note not found"
)

NOTE_NAME_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Travel already has note with such name"
)
