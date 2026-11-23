"""Write the one-sentence journey story for a make.fun bounty entry.

The program writes exactly one short text to <output>/entry.txt, with no
trailing newline, and prints the character count to stderr.
"""

import os
import sys

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on his "
    "last crossing he handed me the wheel at the whistle buoy and stood at the "
    "rail with his back to the town, so I brought us in by the smell of the "
    "cannery and he arrived a passenger."
)


def output_dir() -> str:
    """Folder for entry.txt: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, then /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return value
    return "/output"


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    path = os.path.join(target_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
