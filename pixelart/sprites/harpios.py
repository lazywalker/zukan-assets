"""Harpios, wingdrake. The green skimmer: noios' frame in sea-green with
a taller twin crest."""
from noios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "harpios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (110, 148, 122, 255)  # sea-green body
CONFIG["palette"]["D"] = (82, 116, 94, 255)    # darker green
CONFIG["palette"]["B"] = (150, 178, 158, 255)  # pale wing
CONFIG["palette"]["R"] = (226, 200, 96, 255)   # yellow crest

# taller twin crest
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(4, 5), (7, 8)],
    1:  [(4, 5), (7, 8)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(0, 4, 5), (0, 7, 8)], "R"),
]
