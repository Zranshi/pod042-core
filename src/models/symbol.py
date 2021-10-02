import orm
from src.models.base import all_models, BaseModel


class Symbol(BaseModel):
    tablename = "symbols"
    registry = all_models
    fields = {
        "code": orm.String(max_length=100),
        "symbol": orm.String(max_length=100),
        "name": orm.String(max_length=100),
        **BaseModel.basic,
    }
