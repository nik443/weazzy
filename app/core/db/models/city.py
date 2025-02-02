from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db.models.base_model import BaseModel


class City(BaseModel):
    __tablename__ = "cities"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
