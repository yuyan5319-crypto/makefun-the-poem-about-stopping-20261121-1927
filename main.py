#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt (1 to 280 Unicode code points, per the bounty gate).
"""

import os

POEM = """The next line is already lit.
I could keep going -- the cursor blinks,
the work asking for more.

I stop.
Not because the words ran out,
but the page is full enough.

Stopping is not the absence of doing.
It is the hand that chooses the shore
and lets the tide go on without it."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    print(POEM)

if __name__ == "__main__":
    main()
