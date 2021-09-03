from sqlalchemy import create_engine
from src.orm.base import Base
from src.utils.db import get_url
from src.orm.todo import Todo

if __name__ == "__main__":
    # 创建db连接
    engine = create_engine(get_url(), echo=True)
    # 在数据库中创建数据表
    Base.metadata.create_all(engine)
