from sqlalchemy import String, Result
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import select

from app.core.db.models.base_model import BaseModel
from app.core.db import db_helper


class City(BaseModel):
    __tablename__ = "cities"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    @classmethod
    async def get_city_id_by_name(cls, city_name: str) -> int | None:
        session = db_helper.session_factoty()
        stmt = select(cls.id).filter_by(name=city_name)
        result: Result = await session.execute(stmt)
        city_id = result.scalars().first()
        return city_id
