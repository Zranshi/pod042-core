from fastapi import APIRouter
from src.models.symbol_day import SymbolDay
from src.schema.symbol_day import SymbolDaySchema

router = APIRouter()
SymbolDay.bind_CRUD(router, SymbolDaySchema)
