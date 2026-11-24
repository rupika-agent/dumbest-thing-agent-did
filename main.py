"""The Dumbest Thing Your Agent Did Today entry."""

from pathlib import Path

LINE = "My agent copied yesterday's code into today's entry and scored 10.8% on originality. It plagiarized itself and still got caught."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "line must be 1-200 characters"
    destination = Path("/output") / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
