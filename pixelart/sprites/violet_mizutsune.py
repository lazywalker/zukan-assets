"""Violet Mizutsune, mizutsune subspecies. Pale lavender body with a
taller fin crest and the fan tail split into two deep-violet lobes."""
from mizutsune import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "violet-mizutsune"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (228, 216, 238, 255)  # pale lavender body
CONFIG["palette"]["P"] = (150, 105, 195, 255)  # violet streaks / crest
CONFIG["palette"]["F"] = (120, 70, 170, 255)   # deep violet fan tail
CONFIG["palette"]["C"] = (200, 150, 220, 255)  # lavender bubbles

# taller crest + fan tail split into two lobes by a vertical notch
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(2, 7), (14, 15)],
    3:  [(1, 7), (14, 15)],
    10: [(0, 38), (40, 42)],
    11: [(1, 38), (41, 43)],
    12: [(2, 38), (41, 43)],
    13: [(3, 38), (41, 43)],
    14: [(4, 38), (41, 42)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # violet on the raised crest tip
    ("runs", [(2, 3, 7), (3, 1, 7)], "P", "W"),
]
