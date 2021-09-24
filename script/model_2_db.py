# -*- coding: UTF-8 -*-
# @Time     : 2021/09/03 22:56
# @Author   : Ranshi
# @File     : model_2_db.py
# @Doc      : 根据model创建数据库表

from sqlalchemy import create_engine
from src.orm.base import Base
from src.utils.db import get_url
from src.orm.account import Account

if __name__ == "__main__":
    # 创建db连接
    engine = create_engine(get_url(), echo=True)
    # 在数据库中创建数据表
    Base.metadata.create_all(engine)
