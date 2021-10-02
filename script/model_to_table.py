# -*- coding: UTF-8 -*-
# @Time     : 2021/09/03 22:56
# @Author   : Ranshi
# @File     : model_2_db.py
# @Doc      : 清除所有数据, 并重新创建数据表
from src.models.base import all_models
from src.models.todo import Todo
from src.models.symbol import Symbol
from src.models.symbol_day import SymbolDay

all_models.drop_all()
all_models.create_all()
