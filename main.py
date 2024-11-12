from fastapi import FastAPI, Depends, HTTPException, status, Request
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from routes import signup, login, logout, userinfo

# Load environment variables
load_dotenv()

app = FastAPI()

app.include_router(signup.router, prefix="", tags=["signup"])
app.include_router(login.router, prefix="", tags=["login"])
app.include_router(logout.router, prefix="", tags=["logout"])
app.include_router(userinfo.router, prefix="", tags=["userinfo"])

# static files
app.mount("/app", StaticFiles(directory="./static/", html=True), name="web-app")

@app.get("/app/{path:path}")
async def catch_all():
    return FileResponse("./static/index.html")
