from fastapi import APIRouter, HTTPException
from store import session_store, user_store
import utils
from dto import LoginRequest

router = APIRouter()


@router.post("/login")
async def login(request: LoginRequest):
    """Login user and create a session"""
    user = user_store.get_user_by_username(request.username)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not utils.verify_password(request.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # Create a session
    session_id = session_store.create_session(user["id"])

    # Prepare response
    response = JSONResponse(content={"message": "Login successful"})
    utils.set_session_cookie(response, session_id)
    return response
