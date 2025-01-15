import uvicorn
from fastapi import FastAPI


main_app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app",
        reload=True,
        host="127.0.0.1",
        port=8000,
    )
