# -*- coding: UTF-8 -*-
# @Time     : 2021/09/03 22:56
# @Author   : Ranshi
# @File     : dev_start.py
# @Doc      : 开发环境开始运行

import uvicorn

from src.setting import app

if __name__ == "__main__":
    uvicorn.run(
        app="src.app:app",
        host=app.conf.host,
        port=app.conf.port,
        reload=app.reload,
    )
