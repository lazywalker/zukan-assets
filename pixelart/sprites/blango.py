"""Blango, fanged beast. The blue pack runner: blangonga's baboon frame in
a blue-grey coat, the mustache whiskers and tusks gone, mane tufts and
purple muzzle kept."""
from blangonga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "blango"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (148, 156, 176, 255)  # blue-grey fur
CONFIG["palette"]["C"] = (114, 122, 142, 255)  # darker fur
CONFIG["palette"]["P"] = (90, 78, 116, 255)    # purple muzzle
CONFIG["palette"]["R"] = (148, 156, 176, 255)  # whiskers gone (coat)
CONFIG["palette"]["Y"] = (114, 122, 142, 255)  # tusks gone (fur)

# whisker rows dropped, head rounded
CONFIG["spans"] = {
    **_base["spans"],
    11: [(4, 27)],
    12: [(4, 27)],
    13: [(4, 27)],
    14: [(5, 26)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # tusks recolored back to fur
    ("runs", [(14, 12, 13), (14, 18, 19), (15, 12, 13), (15, 18, 19)],
     "W", "Y"),
]
