"""Boltreaver Astalos, astalos deviant. The black thunder: charcoal
plating with hot yellow lightning over the mantis frame, the crest
forking into twin hot tips."""
from astalos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "boltreaver-astalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (72, 70, 76, 255)     # charcoal plating
CONFIG["palette"]["D"] = (52, 50, 56, 255)     # darker charcoal
CONFIG["palette"]["Y"] = (248, 208, 62, 255)   # hot lightning
CONFIG["palette"]["O"] = (188, 62, 52, 255)    # red chest band

# the crest forked into twin hot tips
CONFIG["spans"] = {
    **_base["spans"],
    7:  [(15, 15), (20, 20)],
    8:  [(15, 16), (19, 20)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(7, 15, 15), (7, 20, 20), (8, 15, 16), (8, 19, 20)], "Y"),
    # hot fork glints on the wings
    ("runs", [(5, 8, 9), (5, 26, 27), (7, 3, 4), (7, 31, 32)], "Y", "D"),
]
