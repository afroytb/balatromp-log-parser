from subprocess import run as _subprocess_run
from pathlib import Path
from json import loads

from balatromp_insights.config import TS_ENTRYPOINT, LOG_PARSER_DIR

def parse_log_file(log_path: str | Path) -> list[dict]:
    """
    Run the TS parseLogSource() function on a Balatro multiplayer log file
    and return the parsed games as a list of dicts.

    Equivalent of: ./run-parse.sh <log_path>
    """
    log_path = Path(log_path).resolve()
    if not log_path.exists():
        raise FileNotFoundError(log_path)

    result = _subprocess_run(
        ["pnpm", "exec", "tsx", str(TS_ENTRYPOINT), str(log_path)],
        cwd=LOG_PARSER_DIR,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"parseLogSource failed (exit {result.returncode}):\n{result.stderr}"
        )

    return loads(result.stdout)