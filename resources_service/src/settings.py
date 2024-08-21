from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseModel):
    host: str = "localhost"
    port: int = 6379
    password: str | None = None


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="_"
    )

    service_port: int
    redis: RedisSettings
    foursquare_key: str
