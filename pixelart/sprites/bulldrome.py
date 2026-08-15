"""Bulldrome, fanged beast. The alpha boar: bullfango's charging frame
grown heavier with a wider body, bigger curved tusks, and a darker
battle-scarred hide."""
from bullfango import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "bulldrome"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (98, 66, 46, 255)     # darker battle hide
CONFIG["palette"]["D"] = (68, 44, 32, 255)     # darker shade
CONFIG["palette"]["C"] = (240, 228, 200, 255)  # bigger pale tusks

# heavier body + bigger tusks
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(0, 14), (15, 17)],
    7:  [(0, 14), (14, 18)],
    8:  [(0, 14), (13, 20)],
    9:  [(0, 14), (12, 21)],
    10: [(0, 14), (12, 22)],
    11: [(1, 14), (12, 23)],
    12: [(1, 14), (12, 23)],
    13: [(2, 14), (12, 23)],
    14: [(3, 14), (12, 23)],
    15: [(4, 13), (12, 22)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # second bigger tusk
    ("runs", [(8, 0, 2), (7, 0, 0)], "C"),
    # scar across the flank
    ("runs", [(12, 16, 17), (13, 18, 19)], "C"),
]
