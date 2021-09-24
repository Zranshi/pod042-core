from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.setting import fastapi as conf
from src.api.base import router

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=conf.allowOrigins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
