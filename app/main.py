from contextlib import asynccontextmanager
from typing import Annotated

import uvicorn
from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.api.crud.user import router as router_user
from app.core.config import settings
from app.core.db.db_helper import db_helper
from app.core.db.models.user import User
from core.db.models import City


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(
    router=router_user,
    prefix="/user",
    tags=["user"],
)


@main_app.get("/all_user/")
async def get_all_users():
    session = db_helper.session_factoty()
    stmt = select(User)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


@main_app.post("/create_city/")
async def create_city(name: str):
    session = db_helper.session_factoty()
    city = City(name=name)
    session.add(city)
    await session.commit()
    return city




if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app",
        reload=True,
        host=settings.run.host,
        port=settings.run.port,
    )
