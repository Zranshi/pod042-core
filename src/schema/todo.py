from src.schema.base import Base


class TodoSchema(Base):
    content: str = ""
    finish: str = "unfinished"
    deadline: str = ""
