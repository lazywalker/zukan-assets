"""Plum Daimyo Hermitaur, daimyo-hermitaur subspecies. Plum-purple shell
over the crab daimyo frame, the helm crest one spike taller."""
from daimyo_hermitaur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "plum-daimyo-hermitaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (140, 84, 138, 255)   # plum shell
CONFIG["palette"]["D"] = (102, 58, 102, 255)   # darker plum
CONFIG["palette"]["C"] = (214, 178, 196, 255)  # pale plum trim

# crest one spike taller
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(14, 15), (23, 24)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(0, 14, 15), (0, 23, 24)], "D"),
]
