# -*- coding: UTF-8 -*-
# @Time     : 2021/10/01 17:45
# @Author   : Ranshi
# @File     : app.py
# @Doc      : 将所有设置附加到app对象上, 供uvicorn调用.
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.base import rootRouter
from src.setting import fastapi as conf

app = FastAPI()
app.include_router(rootRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=conf.allowOrigins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
