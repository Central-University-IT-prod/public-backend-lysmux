from fastapi import HTTPException
from starlette import status

TRAVEL_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Travel not found"
)

TRAVEL_NAME_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already has travel with such a name"
)

PARTICIPANT_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Participant exists"
)

FORBID_ADD_SELF_PARTICIPANT = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Can not add owner as participant"
)
