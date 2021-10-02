import orm
from src.models.base import BaseModel, all_models


class Todo(BaseModel):
    tablename = "todos"
    registry = all_models
    fields = {
        "content": orm.String(max_length=1000, default=""),
        "complete": orm.Boolean(default=False),
        "comment": orm.String(max_length=1000, default="", allow_blank=True),
        **BaseModel.basic,
    }
