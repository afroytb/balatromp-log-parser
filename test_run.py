import sys
from json import dumps

from balatromp_insights.parsers.game_json.json_parser import GameLog

from balatromp_insights.parsers.game_logs.parse_log import parse_log_file
from balatromp_insights.database.init import create_database

from balatromp_insights.config import BASE_DIR
from balatromp_insights.database.connection import get_connection

def main():
    
    path = sys.argv[1] if len(sys.argv) > 1 else None

    if not path:
        print("Usage: python parse_log.py <path-to-log-file>")
        sys.exit(1)
    
    create_database()
    
    # games = parse_log_file(path)
 
    # print(f"Parsed {len(games)} games")
    # print(dumps(games[0], indent=2) if games else "(no games found)")

    game = parse_log_file(path)[0]
    game_log = GameLog.from_json(game)
    print(game_log)

if __name__ == "__main__":
    main()
