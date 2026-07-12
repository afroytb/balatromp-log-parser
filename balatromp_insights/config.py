from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

LOG_PARSER_DIR = BASE_DIR / "balatromp_insights" / "parsers" / "game_logs"
TS_ENTRYPOINT = LOG_PARSER_DIR / "parse-log.mjs"

DATA_DIR = BASE_DIR / "data"

SCHEMA_PATH = BASE_DIR / "balatromp_insights" / "database" / "schema.sql"

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "app.db"