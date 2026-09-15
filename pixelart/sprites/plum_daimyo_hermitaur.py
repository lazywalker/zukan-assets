"""Plum Daimyo Hermitaur, daimyo-hermitaur subspecies. Plum-purple shell
over the crab daimyo frame, the shield crowned with one tall horn."""
from daimyo_hermitaur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "plum-daimyo-hermitaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (140, 84, 138, 255)   # plum shell
CONFIG["palette"]["D"] = (102, 58, 102, 255)   # darker plum
CONFIG["palette"]["C"] = (214, 178, 196, 255)  # pale plum trim

# one tall horn on the shield top
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(18, 19)],
    4:  [(18, 19)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 18, 19), (4, 18, 19)], "D"),
]
