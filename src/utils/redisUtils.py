import json

from redis import ConnectionPool, Redis
from src.setting import redis as conf


class RedisUtils(object):

    _default_conn_pool = None
    _conn = None

    def __init__(self) -> None:
        if not self._default_conn_pool:
            self._default_conn_pool = ConnectionPool(
                host=conf.host,
                port=conf.port,
                password=conf.password,
                db=conf.db
            )
        self._conn = Redis(connection_pool=self._default_conn_pool)

    def delete(self, key):
        return self._conn.delete(key)

    def get_str(self, key):
        value = self._conn.get(key)
        if value:
            return str(value, "utf-8")
        return None

    def set_str(self, key, value, ex=None):
        return self._conn.set(key, value, ex)

    def set(self, key, value, ex=None):
        return self._conn.set(key, json.dumps(value), ex)

    def get(self, key):
        value = self._conn.get(key)
        if value:
            return json.loads(str(value, "utf-8"))
        return None

    def expire(self, key, ex=int):
        return self._conn.expire(key, ex)


# Test
if __name__ == "__main__":
    r = RedisUtils()
    # r.set('sdlf', 'sdfsdflkjxc')
    s = r.get("sdlf")
    print(s)
    r.delete("sdlf")
