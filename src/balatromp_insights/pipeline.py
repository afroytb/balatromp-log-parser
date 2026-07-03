import sys
from json import dumps

from .services.ts_runner import parse_log_file

def run_pipeline():
    path = sys.argv[1] if len(sys.argv) > 1 else None

    if not path:
        print("Usage: python parse_log.py <path-to-log-file>")
        sys.exit(1)
        
    games = parse_log_file(path)

    print(f"Parsed {len(games)} games")
    print(dumps(games[0], indent=2) if games else "(no games found)")