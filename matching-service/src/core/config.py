import os
from logging import config as logging_config
from pathlib import Path

from pydantic import Field, BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

from .logger import LOGGING

logging_config.dictConfig(LOGGING)

BASE_DIR = Path(__file__).parent.parent

class DatabaseConfig(BaseSettings):
    db_host: str = Field("db", alias="DB_HOST")
    db_port: str = Field("5432", alias="DB_PORT")
    db_name: str = Field("db", alias="DB_NAME")
    db_user: str = Field("user", alias="DB_USER")
    db_password: str = Field('secret', alias="POSTGRES_PASSWORD")

    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class RunConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    project_name: str = Field("Auth", alias="PROJECT_NAME")

    run_config: RunConfig = RunConfig()
    db: DatabaseConfig = DatabaseConfig()

settings = Settings()

print(f'postgresql+asyncpg://{settings.db.db_name}:{settings.db.db_password}@{settings.db.db_host}:{settings.db.db_port}/{settings.db.db_user}')

