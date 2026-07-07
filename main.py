import sys
from json import dumps

from balatromp_insights.parsers.game_logs.parse_log import parse_log_file

def main():
    
    path = sys.argv[1] if len(sys.argv) > 1 else None

    if not path:
        print("Usage: python parse_log.py <path-to-log-file>")
        sys.exit(1)
        
    games = parse_log_file(path)

    print(f"Parsed {len(games)} games")
    print(dumps(games[0], indent=2) if games else "(no games found)")

if __name__ == "__main__":
    main()