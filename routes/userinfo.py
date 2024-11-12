from store import user_store
from typing import Union
from fastapi import APIRouter
from models.user import User, UserReadError
from middleware import auth_required

router = APIRouter()


@router.get(
    "/users/{username}",
    response_model=Union[User, UserReadError],
    responses={404: {"model": UserReadError}},
)
@auth_required
def get_user(username: str):
    user = user_store.get_user_by_username(username)
    if user:
        return user
    else:
        return UserReadError(error_code=404, message="User not found")
