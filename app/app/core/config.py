from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host = "127.0.0.1"
    port = 8000


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echoo: bool
    echo_pool = False
    max_overflow = 10
    pool_size = 50

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env-template",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run = RunConfig()
    db: DatabaseConfig


settings = Setting()
