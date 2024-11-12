from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    password: str


class UserReadError(BaseModel):
    error_code: int
    message: str