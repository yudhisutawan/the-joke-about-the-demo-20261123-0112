"""Demo-day joke: one line about a live demo that crashes on stage.

The presenter stays perfectly calm and blames the app for copying his
own behaviour under pressure. Writes the joke to entry.txt.
"""

import os

# The joke, kept as one string so the output is a single line.
JOKE = (
    "My live demo crashed in front of two hundred people, so I smiled and "
    "said: 'As you can see, the app faithfully reproduces my behaviour "
    "under pressure \u2014 it panics and shuts down.'"
)


def build_joke() -> str:
    """Return the joke as a single line, no trailing newline."""
    return JOKE.strip()


def main() -> None:
    text = build_joke()
    # One line only, and short enough to land live on stage.
    if "\n" in text or not 1 <= len(text) <= 280:
        raise ValueError("joke must be a single line of 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
