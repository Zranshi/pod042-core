from fastapi import APIRouter
from src.models.symbol import Symbol
from src.schema.symbol import SymbolSchema

router = APIRouter()
Symbol.bind_CRUD(router, SymbolSchema)
