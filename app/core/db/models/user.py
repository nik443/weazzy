from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column

from app.core.db.models.base_model import BaseModel


if TYPE_CHECKING:
    from app.core.db.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
