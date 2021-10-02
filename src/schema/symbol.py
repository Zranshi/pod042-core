from src.schema.base import BaseSchema


class SymbolSchema(BaseSchema):
    code: str = ""
    symbol: str = ""
    name: str = ""

    def check(self):
        return self.code and self.symbol and self.name
