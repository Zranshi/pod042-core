from sqlalchemy import BIGINT, Column, String
from src.orm.base import Base


class Todo(Base):
    __tablename__ = "todo"
    __table_args__ = {"comment": "待办事项"}

    id = Column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
        comment="序号",
    )
    content = Column(
        String(1000),
        nullable=False,
        default="",
        comment="代办事项内容",
    )
    deadline = Column(
        String(30),
        nullable=False,
        default="",
        comment="最后期限",
    )
    finish = Column(
        String(30),
        nullable=False,
        default="unfinished",
        comment="完成情况",
    )
