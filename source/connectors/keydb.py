import redis
from config import settings


class KeyDB(redis.Redis):
    def __init__(self, host="localhost", port=6379, db=0, **kwargs):
        username = kwargs.get("username") or settings.get("keydb.username")
        password = kwargs.get("password") or settings.get("keydb.password")
        super().__init__(
            host=settings.get("keydb.host") or host,
            port=settings.get("keydb.port") or port,
            db=settings.get("keydb.db") or db,
            username=username or None,
            password=password or None,
        )
