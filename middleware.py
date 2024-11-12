from fastapi import FastAPI, HTTPException, Request
from functools import wraps

# Auth Middleware
def auth_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")
        print("yeeeee, middleware works!")
        # TODO: check if request authenticated
        # api_key = request.headers.get("X-API-Key")
        # if api_key != "mysecretkey":
        #     raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")
        return await func(*args, **kwargs)

    return wrapper
