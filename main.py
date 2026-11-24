"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line to /output/entry.txt: a code review comment that
approves a pull request while carrying quiet existential dread.
Deterministic: the same text on every run.
"""

import os

COMMENT = "LGTM. It works today, which is more than I can say for most things, including me."


def validate(text: str) -> str:
    text = text.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
    assert text.startswith(("LGTM", "Approved")), "entry must approve the PR"
    return text


def main() -> None:
    text = validate(COMMENT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
