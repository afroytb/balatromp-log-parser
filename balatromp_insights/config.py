from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[0]

WEB_PARSER_DIR = BASE_DIR / "web_parser"
TS_ENTRYPOINT = WEB_PARSER_DIR / "parse-log.mjs"
