# -*- coding: UTF-8 -*-
# @Time     : 2021/09/03 18:34
# @Author   : Ranshi
# @File     : db_setting.py
# @Doc      : 获取数据库连接url

from src.setting import db as conf
from databases import Database


def database_connection() -> Database:
    if conf.dbType == "sqlite":
        return Database(sqlite_url(conf.sqlite))
    elif conf.dbType == "mysql":
        return Database(mysql_url(conf.mysql))
    return ""


def sqlite_url(conf) -> str:
    return "sqlite:///{file_path}".format(
        file_path=conf.dbFile,
    )


def mysql_url(conf) -> str:
    return "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(
        username=conf.usr,
        password=conf.pwd,
        host=conf.host,
        port=conf.port,
        db=conf.dbName,
    )
