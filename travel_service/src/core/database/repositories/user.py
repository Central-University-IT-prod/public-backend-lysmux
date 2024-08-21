from core.database.models import UserModel
from .base import BaseRepository


class UserRepository(BaseRepository):
    model_type = UserModel
