import asyncio

from pydantic import BaseModel, Field, field_validator, model_validator

from core.db.models import User


class UserCreate(BaseModel):
    username: str = Field(description="Имя пользователя при регистрации")
    age: int | None = Field(description="Возраст пользователя при регистрации")
    city_name: str = Field(description="Название города проживания пользователя при регистрации")

    @field_validator("username", mode="before")
    def validate_username(cls, username: str):  # noqa
        if not username:
            raise ValueError("Username field is empty")
        if len(username) > 40:
            raise ValueError("Username field must be < 40 symbols")
        return username

    @field_validator("age", mode="before")
    def validate_age(cls, age: int | None):  # noqa
        if isinstance(age, int):
            if age < 0:
                raise ValueError("Age field must be > 0")
            if age > 122:
                raise ValueError("Age field must be < 122")
            return age
        if age is not None:
            raise ValueError("Age field must have type in [int, None]")
