from pydantic import BaseModel
from src.utils.bind_schema_data import bind


class Base(BaseModel):
    def new_obj(self, obj, ignore=set()) -> object:
        return bind(obj, self, ignore)
