# -*- coding: UTF-8 -*-
# @Time     : 2021/09/01 17:26
# @Author   : Ranshi
# @File     : __init__.py
# @Doc      : 配置文件

import yaml

from src.utils.dot_dict import DotDict

with open("docs/conf.yaml") as config:
    conf = DotDict(yaml.load(config.read(), Loader=yaml.FullLoader))

fastapi = conf.fastapi
app = conf.app
app.conf = app.dev if app.isDev else app.pro
app.pop("dev")
app.pop("pro")

db = conf.db
redis = conf.redis
