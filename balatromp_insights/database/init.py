import sqlite3

from balatromp_insights.database.connection import get_connection
# from balatromp_insights.database.seed import seed 

from balatromp_insights.config import SCHEMA_PATH

def create_database():
    with open(SCHEMA_PATH) as f:
        schema = f.read()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.executescript(schema)