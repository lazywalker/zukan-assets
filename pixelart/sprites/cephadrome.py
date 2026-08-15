"""Cephadrome, piscine wyvern. The sand swimmer: green-yellow hide over
the mud-fish frame, a tall sand-fin crest, pale sand dust along the back,
and the grin kept."""
from jyuratodus import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "cephadrome"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (158, 168, 106, 255)  # green-yellow hide
CONFIG["palette"]["D"] = (124, 134, 80, 255)   # darker shade
CONFIG["palette"]["R"] = (206, 190, 130, 255)  # sand fin
CONFIG["palette"]["C"] = (216, 210, 166, 255)  # pale belly

# taller sand-fin crest
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(6, 12), (15, 17)],
    5:  [(4, 15), (15, 19)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 15, 17), (5, 16, 18)], "R"),
]
