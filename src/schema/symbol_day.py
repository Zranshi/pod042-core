from src.schema.base import BaseSchema


class SymbolDaySchema(BaseSchema):
    code: str = ""
    day: str = ""
    start_price: float = 0.0
    end_price: float = 0.0
    high_price: float = 0.0
    low_price: float = 0.0
    volume: int = 0.0
    volume_price: float = 0.0
    change_rate: float = 0.0
