"""Gajios, leviathan. The water monitor: jagras' little frame in a wet
blue-grey coat with a longer snout and fin crest."""
from jagras import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gajios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (110, 128, 140, 255)  # wet blue-grey scales
CONFIG["palette"]["D"] = (80, 96, 108, 255)    # darker blue
CONFIG["palette"]["Y"] = (150, 170, 182, 255)  # pale fin crest
CONFIG["palette"]["O"] = (150, 160, 150, 255)  # grey belly

# longer snout + taller fin crest
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(2, 6), (10, 10), (13, 13)],
    5:  [(1, 7), (9, 10), (12, 13), (14, 14)],
    6:  [(0, 7), (9, 10), (13, 13), (15, 15)],
}
