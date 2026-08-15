"""Meraginasu, elder dragon. The eclipse steed: black-gold armor with a
gold trim line along the back, and a jagged gold-spined ridge replacing
the parent's smooth back edge."""
from estrellian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "meraginasu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (48, 44, 50, 255)     # black armor hide
CONFIG["palette"]["D"] = (34, 32, 36, 255)     # darkest hide
CONFIG["palette"]["R"] = (222, 178, 82, 255)   # gold horns
CONFIG["palette"]["r"] = (196, 150, 64, 255)   # darker far horn
CONFIG["palette"]["Y"] = (222, 178, 82, 255)   # gold trim / stars

# jagged spine ridge along the back
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(0, 7), (8, 13), (17, 18)],
    7:  [(0, 15), (17, 19), (22, 23)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # gold trim along the back
    ("runs", [(9, 14, 15), (10, 16, 17), (11, 18, 19), (12, 20, 21)],
     "Y", "N"),
    # the spine spikes gilded
    ("runs", [(6, 17, 18), (7, 17, 19), (7, 22, 23)], "Y"),
]
