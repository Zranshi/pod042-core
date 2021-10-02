from src.schema.base import BaseSchema


class TodoSchema(BaseSchema):
    content: str = ""
    complete: bool = False
    comment: str = ""
