"""Gonngenn Daimyo Hermitaur, daimyo-hermitaur variant. The golden daimyo:
gold shell over the crab daimyo frame with a twin-horned crown."""
from daimyo_hermitaur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gonngenn-daimyo-hermitaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (208, 172, 82, 255)   # gold shell
CONFIG["palette"]["D"] = (164, 132, 56, 255)   # darker gold

# twin-horned crown rising from the gold dome
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(17, 17), (20, 20)],
    4:  [(17, 17), (20, 20)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 17, 17), (3, 20, 20), (4, 17, 17), (4, 20, 20)], "D"),
]
