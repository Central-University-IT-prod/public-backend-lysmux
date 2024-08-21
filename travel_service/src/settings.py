from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    service_port: int

    postgres_username: str
    postgres_password: str
    postgres_host: str
    postgres_port: int = 5432
    postgres_database: str

    @computed_field
    @property
    def database_url(self) -> URL:
        url = URL.create(
            drivername="postgresql+asyncpg",
            username=self.postgres_username,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_database
        )
        return url
