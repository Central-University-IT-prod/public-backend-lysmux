from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

LOG_LEVELS = Literal["DEBUG", "INFO", "ERROR"]


class RedisSettings(BaseModel):
    host: str = "localhost"
    port: int = 6379
    password: str | None = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="_"
    )

    log_level: LOG_LEVELS = "INFO"

    redis: RedisSettings = RedisSettings()

    bot_token: str

    resources_service_host: str
    resources_service_port: int

    travel_service_host: str
    travel_service_port: int
