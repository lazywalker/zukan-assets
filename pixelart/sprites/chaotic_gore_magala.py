"""Chaotic Gore Magala, gore-magala variant. The half-shed chaos: grey-
violet frame, one gold eye open, and the half-grown wing rising from the
cloak's back edge while the hem stays ragged."""
from gore_magala import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "chaotic-gore-magala"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (74, 66, 88, 255)     # grey-violet body
CONFIG["palette"]["D"] = (56, 50, 70, 255)     # darker violet
CONFIG["palette"]["P"] = (150, 120, 185, 255)  # brighter ragged hem
CONFIG["palette"]["V"] = (222, 178, 82, 255)   # one gold eye open

# the half-grown wing rises from the cloak's back edge
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(6, 7), (11, 11), (20, 21)],
    5:  [(5, 7), (10, 12), (18, 22)],
    6:  [(4, 9), (9, 13), (17, 23)],
    7:  [(3, 10), (8, 23)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the half-grown wing: violet membrane with a gold rim
    ("runs", [(5, 18, 22), (6, 17, 23)], "D"),
    ("runs", [(4, 20, 21), (5, 21, 22), (6, 22, 23)], "V"),
    # the gold eye replaces the pale one
    ("put", 6, 5, "V"),
]
