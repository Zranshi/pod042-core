import uvicorn

from src.setting import app

if __name__ == "__main__":
    uvicorn.run(
        app=app.uvicornRunAppScript,
        host=app.conf.host,
        port=app.conf.port,
        reload=app.reload,
    )
