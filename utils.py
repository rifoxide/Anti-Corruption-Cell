from fastapi.responses import JSONResponse
from hashlib import sha256


# Hash password function
def hash_password(password: str) -> str:
    """Hash the password using sha256"""
    return sha256(password.encode("utf-8")).hexdigest()


# Verify password (you can adjust this to check against your database)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if the password matches the stored hash"""
    return hash_password(plain_password) == hashed_password


# Function to set a cookie (session id)
def set_session_cookie(response: JSONResponse, session_id: str):
    """Set session cookie with a simple identifier"""
    response.set_cookie(
        key="session_id",
        value=session_id,
        # httponly=True,  # Prevents JavaScript from accessing it
        # max_age=3600,  # 1 hour expiration
        # secure=True,  # Use HTTPS in production
    )
