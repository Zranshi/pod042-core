# -*- coding: UTF-8 -*-
# @Time     : 2021/09/01 17:26
# @Author   : Ranshi
# @File     : __init__.py
# @Doc      : 配置文件

import json

from src.utils.dot_dict import DotDict

with open("docs/conf.json") as config:
    conf = DotDict(json.load(config))

fastapi = conf.fastapi
app = conf.app
app.conf = app.dev if app.isDev else app.pro
app.pop("dev")
app.pop("pro")

db = conf.db
redis = conf.redis
