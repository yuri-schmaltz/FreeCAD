#!/usr/bin/env python3
"""Fail if a TODO comment lacks an issue reference."""
import sys
import re
from pathlib import Path

TODO_RE = re.compile(r"TODO\(#[0-9]+\)")


def main(paths: list[str]) -> int:
    failed = False
    for path_str in paths:
        if Path(path_str).name == "check_todo.py":
            continue
        path = Path(path_str)
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            if "TODO" in line and not TODO_RE.search(line):
                print(f"{path}:{lineno}: TODO missing issue reference")
                failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
