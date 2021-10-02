from pydantic import BaseModel
from src.utils.dot_dict import DotDict


class BaseSchema(BaseModel):
    def dict(self) -> DotDict:
        return DotDict(self.__dict__)
