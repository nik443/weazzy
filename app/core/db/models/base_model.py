from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from app.core.config import settings
from app.utils.utils import camel_to_snake_case


class BaseModel(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_to_snake_case(cls.__name__)}"

    id: Mapped[int] = mapped_column(primary_key=True)
