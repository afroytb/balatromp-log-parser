import sqlite3

from balatromp_insights.config import DATABASE_DIR, DATABASE_PATH

def get_connection() -> sqlite3.Connection:
    DATABASE_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    return conn
