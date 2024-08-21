from fastapi import HTTPException
from starlette import status

LOCATION_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Location not found"
)

LOCATION_NAME_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Travel already has location with such name"
)
