from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


main_app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app",
        reload=True,
        host=settings.run.host,
        port=settings.run.port,
    )
