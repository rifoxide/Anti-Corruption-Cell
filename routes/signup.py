from fastapi import APIRouter
from dto import SignUpRequest
from store import user_store
from fastapi import HTTPException
import utils
from db import get_db_connection

router = APIRouter()


@router.post("/signup")
async def signup(request: SignUpRequest):
    """Sign up new user and store their details"""
    # Check if the username already exists
    username = request.username
    password = request.password
    existing_user = user_store.get_user_by_username(username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the user's password before storing it
    hashed_password = utils.hash_password(password)

    # Insert the new user into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, hashed_password),
    )
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "User created successfully"}
