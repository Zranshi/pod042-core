from fastapi import APIRouter
from src.api.symbol import router as symbol
from src.api.todo import router as todos
from src.setting import app
from starlette.responses import RedirectResponse
from src.api.symbol_day import router as symbol_day

baseRouter = APIRouter()

baseRouter.include_router(todos, tags=["todos"], prefix="/todo")
baseRouter.include_router(symbol, tags=["symbol"], prefix="/symbol")
baseRouter.include_router(symbol_day, tags=["symbol_day"], prefix="/symbol_day")


@baseRouter.get("/", tags=["root"])
async def read_root() -> dict:
    return RedirectResponse(url=f"http://{app.conf.host}:{app.conf.port}/docs")
