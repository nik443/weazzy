from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    age: int
    city_name: str
    