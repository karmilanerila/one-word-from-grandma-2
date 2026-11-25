"""One Word From Grandma: the single word grandma texts about AI.

Grandma never learned the machine's name. When the grandkids show her the
glowing box that answers questions and writes poems, she squints at it,
pats it like a toaster, and calls it the Doohickey -- the warm, slightly
baffled name she gives every gadget she cannot quite name.
"""

import os

WORD = "Doohickey"


def validate(word):
    """Keep the entry inside the gate: one word, 1-30 chars, no spaces."""
    if not word or len(word) > 30:
        raise ValueError("entry must be 1-30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word")
    return word


def output_path():
    """Resolve where the entry goes, honouring the grader's output dir."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    word = validate(WORD)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write((word + "\n").encode("utf-8"))
    os.chmod(path, 0o644)
    print("wrote %s to %s" % (word, path))


if __name__ == "__main__":
    main()
