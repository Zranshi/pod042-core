from fastapi import APIRouter
from src.api.todo import router as todos
from src.setting import app
from starlette.responses import RedirectResponse

router = APIRouter()

router.include_router(todos, tags=["todos"], prefix="/todo")


@router.get("/", tags=["root"])
async def read_root() -> dict:
    return RedirectResponse(url=f"http://{app.conf.host}:{app.conf.port}/docs")
