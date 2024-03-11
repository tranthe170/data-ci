from contextlib import contextmanager
from dataclasses import dataclass

import psycopg2


@dataclass
class DBConnection:
    db: str
    user: str
    password: str
    host: str
    port: int = 5432


class WarehouseConnection:
    def __init__(self, db_connection: DBConnection):
        self.conn_url = (
            f"postgresql://{db_connection.user}:{db_connection.password}@"
            f"{db_connection.host}:{db_connection.port}/{db_connection.db}"
        )

    @contextmanager
    def managed_cursor(self, cursor_factory=None):
        self.conn = psycopg2.connect(self.conn_url)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor(cursor_factory=cursor_factory)
        try:
            yield self.cursor
        finally:
            self.cursor.close()
            self.conn.close()
