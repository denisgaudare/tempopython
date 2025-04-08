
import logging
import sqlite3
from datetime import datetime


class SQLiteHandler(logging.Handler):
    def __init__(self, db_path="pipeline_logs.db"):
        super().__init__()
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    timestamp TEXT,
                    level TEXT,
                    step TEXT,
                    message TEXT
                )
            """)

    def emit(self, record):
        with self.conn:
            self.conn.execute(
                "INSERT INTO logs (timestamp, level, step, message) VALUES (?, ?, ?, ?)",
                (datetime.utcnow().isoformat(), record.levelname, record.name, record.getMessage())
            )
