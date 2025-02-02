import os

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DatabaseConfig(BaseModel):
    # url: str = os.getenv("DB__URL")
    url: str = "postgresql+asyncpg://postgres:1111@localhost:5432/weazzy"
    echo: bool = bool(os.getenv("DB__ECHO"))
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 50

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Setting(BaseSettings):
    # model_config = SettingsConfigDict(
    #     env_file=".env-template",  # файл с кредами
    #     case_sensitive=False,  # учитывать регистр имен кредов
    #     env_nested_delimiter="__",  # разделитель вложенных значений env
    # )
    run: RunConfig = RunConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Setting()
a = 4