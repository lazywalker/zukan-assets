"""Shrieking Legiana: the screaming ice wyvern. Pale ice palette, crest
antennae raised straight up, and the beak split open mid-shriek."""
from legiana import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shrieking-legiana"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (192, 206, 232, 255)
CONFIG["palette"]["D"] = (140, 155, 200, 255)
CONFIG["palette"]["W"] = (246, 242, 230, 255)

# antennae up one row, beak split open by a 1px channel
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(5, 8), (11, 11), (18, 18), (25, 28)],
    7:  [(1, 9), (10, 14), (16, 19), (20, 28)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # ice breath in the open beak
    ("put", 6, 15, "W"),
]
