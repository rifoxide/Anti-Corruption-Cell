from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    status: str

class LoginError(BaseModel):
    error: str

class SignUpRequest(BaseModel):
    username: str
    password: str
