# -*- coding: UTF-8 -*-
# @Time     : 2021/09/01 21:22
# @Author   : Ranshi
# @File     : __init__.py
# @Doc      : Model, 数据表对象
from fastapi import APIRouter

from .user import router as user

modelsAPI = APIRouter()


modelsAPI.include_router(user, tags=["user"], prefix="/user")
