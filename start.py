#!/usr/bin/env python
import uvicorn
from src.setting import app

if __name__ == "__main__":
    uvicorn.run(
        app="src.app:app",
        host=app.conf.host,
        port=app.conf.port,
    )
