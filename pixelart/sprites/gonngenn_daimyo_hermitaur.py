"""Gonngenn Daimyo Hermitaur, daimyo-hermitaur variant. The golden daimyo:
gold shell over the crab daimyo frame with a taller crown."""
from daimyo_hermitaur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gonngenn-daimyo-hermitaur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (208, 172, 82, 255)   # gold shell
CONFIG["palette"]["D"] = (164, 132, 56, 255)   # darker gold

# taller crown
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(13, 14), (18, 19), (24, 25)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(0, 13, 14), (0, 18, 19), (0, 24, 25)], "D"),
]
