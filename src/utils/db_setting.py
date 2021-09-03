# -*- coding: UTF-8 -*-
# @Time     : 2021/09/03 18:34
# @Author   : Ranshi
# @File     : db_setting.py
# @Doc      : 获取数据库连接url

from src.setting import db as conf


def get_url() -> str:
    if conf.dbType == "sqlite":
        return sqlite_url(conf.sqlite)


def sqlite_url(conf) -> str:
    return f"sqlite:///{conf.dbFile}"
