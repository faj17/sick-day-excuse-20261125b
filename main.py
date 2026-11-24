"""The funniest sick-day excuse — make.fun bounty.

One line, 123 characters, that someone could send to their boss to call
in sick: the locksmith is drilling out the front door because the keys
are locked inside — and, technically, so is the sender. The script
validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The excuse itself: one line, exactly 123 characters.
# The premise (locked door, locksmith on the way) is half believable;
# the twist — the sender is locked inside too — lands on the last words.
EXCUSE = (
    "Won't be in today \u2014 the locksmith is drilling out my front "
    "door because my keys are locked inside, and technically so am I."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the excuse; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"excuse must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if not text:
        raise ValueError("excuse must not be only whitespace")
    return text


def main() -> None:
    text = validate(EXCUSE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
