"""Boltreaver Astalos, astalos deviant. The black thunder: charcoal plating
with hot yellow lightning over the mantis frame."""
from astalos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "boltreaver-astalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (72, 70, 76, 255)     # charcoal plating
CONFIG["palette"]["D"] = (52, 50, 56, 255)     # darker charcoal
CONFIG["palette"]["Y"] = (248, 208, 62, 255)   # hot lightning
CONFIG["palette"]["O"] = (188, 62, 52, 255)    # red chest band

# the black thunder: the crest horn forks into twin hot tips
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(6, 6), (9, 9)],
    2:  [(5, 10)],
    3:  [(4, 11), (29, 31)],
}
