"""
Python wrapper around the TypeScript `parseLogSource` function
(json_parser/log-source-parser.ts, called via parse-log.mjs).

Requirements: Node.js + npm on PATH (tsx gets installed automatically
into log_parser/node_modules on first run).

Usage:
    from parse_log import parse_log_file
    games = parse_log_file("sample.log")
    # games is a list[dict], one dict per ParsedLogGame -- feed straight
    # into pandas.DataFrame(games) to start your dataviz.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

PARSER_DIR = Path(__file__).parent
ENTRY_SCRIPT = PARSER_DIR / "web_parser" / "parse-log.mjs"


def _ensure_deps_installed() -> None:
    """Install node deps (tsx) into log_parser/node_modules if missing."""
    if not (PARSER_DIR / "node_modules" / "tsx").exists():
        subprocess.run(
            ["pnpm", "install", "--no-audit", "--no-fund"],
            cwd=PARSER_DIR,
            check=True,
            capture_output=True,
        )


def parse_log_file(log_path: str | Path) -> list[dict]:
    """
    Run the TS parseLogSource() function on a Balatro multiplayer log file
    and return the parsed games as a list of dicts.

    Equivalent of: ./run-parse.sh <log_path>
    """
    log_path = Path(log_path).resolve()
    if not log_path.exists():
        raise FileNotFoundError(log_path)

    _ensure_deps_installed()

    result = subprocess.run(
        ["pnpm", "exec", "tsx", str(ENTRY_SCRIPT), str(log_path)],
        cwd=PARSER_DIR,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"parseLogSource failed (exit {result.returncode}):\n{result.stderr}"
        )

    return json.loads(result.stdout)


def parse_log_text(log_text: str) -> list[dict]:
    """Same as parse_log_file, but takes the raw log content as a string."""
    tmp = PARSER_DIR / "_tmp_input.log"
    tmp.write_text(log_text, encoding="utf-8")
    try:
        return parse_log_file(tmp)
    finally:
        tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else None
    if not path:
        print("Usage: python parse_log.py <path-to-log-file>")
        sys.exit(1)

    games = parse_log_file(path)
    print(f"Parsed {len(games)} games")
    print(json.dumps(games[0], indent=2) if games else "(no games found)")