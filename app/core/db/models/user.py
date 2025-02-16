from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Integer, select, Result
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db.models.base_model import BaseModel
from app.core.db import db_helper

if TYPE_CHECKING:
    from app.core.db.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, unique=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey("cities.id"))
