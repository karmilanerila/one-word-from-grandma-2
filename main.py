"""Thingy: the one word grandma texts about AI.

Grandma never learned the machine's name, so she calls it Thingy --
the warm, baffled pet name for the all-powerful box on the table.
"""

import os

WORD = "Thingy"


def write_entry(word):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


def main():
    write_entry(WORD)


if __name__ == "__main__":
    main()
