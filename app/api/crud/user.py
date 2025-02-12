from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.api.schemas import UserCreate
from app.core.db import db_helper
from core.db.models import City


router = APIRouter()


async def _get_user_city_id(city_name: str | None) -> City | None:
    session = db_helper.session_factoty()
    stmt = select(City).filter_by(name=city_name)
    result: Result = await session.execute(stmt)
    city_db = result.scalars().first()
    return city_db


@router.post("/create/")
async def create_user(user_city: Annotated[int, Depends(_get_user_city_id)]) -> dict:
    if user_city is None:
        return {"status": "400", "detail": "bad request"}

    return {"status": "200", "detail": "user create"}
