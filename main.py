#!/usr/bin/env python3
"""One-line office joke entry: writes the chosen joke to /output/entry.txt."""

import os

JOKE = "My manager booked a meeting about why we have too many meetings: 45 minutes, 18 people, one agenda item \u2014 'meeting culture.' I declined. He rescheduled it."


def main():
    text = JOKE + "\n"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
