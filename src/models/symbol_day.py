import orm
from src.models.base import BaseModel, all_models


class SymbolDay(BaseModel):
    tablename = "symbol_day"
    registry = all_models
    fields = {
        "code": orm.BigInteger(),
        "day": orm.Date(),
        "start_price": orm.Float(),
        "end_price": orm.Float(),
        "high_price": orm.Float(),
        "low_price": orm.Float(),
        "volume": orm.BigInteger(),
        "volume_price": orm.Float(),
        "change_rate": orm.Float(),
        **BaseModel.basic,
    }
