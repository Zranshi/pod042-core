from src.schema.base import Base


class TodoSchema(Base):
    id: int = 0
    content: str
    finish: str = "unfinished"
    deadline: str = ""
