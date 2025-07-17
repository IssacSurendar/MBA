from fastapi import FastAPI
from routers.users import router as user_router
from routers.attendance import router as attendance_router
import asyncio
from core.utils import clear_pycache

app = FastAPI()

app.include_router(user_router)
app.include_router(attendance_router)
clear_pycache()