from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[0]

LOG_PARSER_DIR = BASE_DIR / "parsers" / "game_logs"
TS_ENTRYPOINT = LOG_PARSER_DIR / "parse-log.mjs"
