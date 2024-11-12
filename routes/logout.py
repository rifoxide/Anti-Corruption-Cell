from fastapi import APIRouter, HTTPException, Request
from store import session_store, user_store
import utils
from dto import LoginRequest
from fastapi.responses import JSONResponse
from middleware import auth_required

router = APIRouter()

@router.post("/logout")
@auth_required
async def logout(request: Request):
    """ Logout and delete the session """
    session_id = request.cookies.get("session_id")
    if session_id:
        session_store.delete_session(session_id)

    response = JSONResponse(content={"message": "Logged out successfully"})
    response.delete_cookie("session_id")
    return response