from typing import Optional
from dotenv import load_dotenv
from redis import Redis, ConnectionError

from config import config


load_dotenv()


class RedisConnection:
    def __init__(
        self,
        host: str = config.REDIS_HOST,
        port: int = config.REDIS_PORT,
        db: int = 0,
        password: Optional[str] = config.REDIS_PASSWORD,
        url: Optional[str] = config.REDIS_URL,
    ):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.connection = None
        self.url = self.construct_url() if not url else url

    def construct_url(self) -> str:
        password_section = f":{self.password}@" if self.password else ""
        return f"redis://{password_section}{self.host}:{self.port}/{self.db}"

    def _get_redacted_url(self) -> str:
        password_section = f":{'*' * len(self.password)}@" if self.password else ""
        return f"redis://{password_section}{self.host}:{self.port}/{self.db}"

    def connect(self) -> None:
        try:
            print(f"Connecting to Redis at host: {self.host}:{self.port}", flush=True)
            self.connection = Redis(
                host=self.host,
                port=self.port,
                db=self.db,
                password=self.password,
            )

            pong = self.connection.ping()
            if pong:
                print(f"Connected to Redis at {self._get_redacted_url()}")
        except ConnectionError:
            raise Exception("Cannot connect to Redis")

    def get_connection(self) -> Redis:
        if not self.connection:
            self.connect()
        return self.connection


redis_conn = RedisConnection()
redis_client = redis_conn.get_connection()
