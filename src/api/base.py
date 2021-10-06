from fastapi import APIRouter
from src.models import modelsAPI
from src.setting import app
from starlette.responses import RedirectResponse

from .entrance import router as entrance

rootRouter = APIRouter()

rootRouter.include_router(modelsAPI, prefix="/models")

rootRouter.include_router(entrance, tags=["entrance"], prefix="/entrance")


@rootRouter.get("/", tags=["root"])
async def read_root() -> dict:
    return RedirectResponse(url=f"http://{app.conf.host}:{app.conf.port}/docs")
