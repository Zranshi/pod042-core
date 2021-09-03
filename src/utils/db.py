from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from src.utils.db_setting import get_url
from src.setting import db as conf


class DbUtils(object):
    sess: Session = None

    def __init__(self) -> None:
        self.sess = self._create_scoped_session(get_url())

    @staticmethod
    def _create_scoped_session(url: str):
        engine = create_engine(url, echo=conf.echo)
        return scoped_session(
            sessionmaker(autocommit=True, autoflush=False, bind=engine)
        )

    @staticmethod
    def _get_file(file_name):
        with open(f"app/sql/{file_name}", "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def get_sql_by_file(file_name, params={}):
        sql = DbUtils._get_file(file_name)
        return sql.format(**params)


db = DbUtils()
