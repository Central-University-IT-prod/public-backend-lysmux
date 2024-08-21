from fastapi import HTTPException
from starlette import status

USER_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found"
)

USER_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exist"
)
