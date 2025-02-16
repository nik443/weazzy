from typing import Annotated

from fastapi import APIRouter, Depends, Response
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.api.schemas import UserCreate
from core.db.models import City


router = APIRouter()


@router.post("/create/")
async def create_user(user: UserCreate, response: Response) -> dict:
    city_id_db = await City.get_city_id_by_name(city_name=user.city_name)

    if not city_id_db:
        response.status_code = 400
        return {"status": "400", "detail": "This city not found in DB"}

    return {"status": "200", "detail": "user create"}