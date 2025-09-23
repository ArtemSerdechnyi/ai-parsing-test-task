import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi"
    READER_DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi"
    SYNC_WRITER_DB_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/fastapi"
    SYNC_READER_DB_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/fastapi"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = ""
    # CELERY_BROKER_URL: str = "amqp://user:bitnami@localhost:5672/"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    # CELERY_BACKEND_URL: str = "redis://:password123@localhost:6379/0"
    CELERY_BACKEND_URL: str = "redis://localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    OPENAI_API_KEY: str

    UPLOADED_FILES_DIRECTORY: Path = ROOT_DIR / "core" / "uploaded_files"


class TestConfig(Config):
    WRITER_DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi_test"
    READER_DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi_test"


class LocalConfig(Config):
    ...


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "test": TestConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()