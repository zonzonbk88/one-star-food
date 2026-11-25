#!/usr/bin/env python3
"""One Star, Five Stars for the Food (u-po-pu-one-star-five-stars-for-the-food-f9166ee7).

Writes exactly one sentence — a one-star review of Earth by an alien
tourist that still compliments the food — to entry.txt with no trailing
newline. Standard library only.
"""

import os

ENTRY = (
    "The locals point glowing rectangles at their food and wait for it to go "
    "cold before eating, which earns the one star, though the cold noodles "
    "were still the best meal in this galaxy."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
