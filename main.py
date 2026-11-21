"""Write one short, slow text to /output/entry.txt.

The text is a fixed string: rain stopping, a kettle clicking off, a cat
asleep where the sun was, a clock ticking, and the dark past the window
keeping on deepening. Nothing in it tells the reader to relax; the
slowness is in the sentences themselves, and the last image keeps growing
after the last line.
"""

import os

TEXT = (
    "Rain has stopped on the roof. The kettle clicks off; "
    "steam rises, thins, is gone. A cat sleeps where the sun was. "
    "Nothing tonight asks you to hurry. The clock ticks once, then again, "
    "and the dark past the window keeps deepening, as if it had all the "
    "time in the world."
)


def main() -> None:
    # The gate allows 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
