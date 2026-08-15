"""Piragill, leviathan. The gill fin: epioth's little frame in a wet teal
coat with big gill fins flaring off the head."""
from epioth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "piragill"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (108, 158, 152, 255)  # wet teal scales
CONFIG["palette"]["D"] = (80, 124, 120, 255)   # darker teal
CONFIG["palette"]["C"] = (188, 216, 210, 255)  # pale belly

# gill fins flaring off the head
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(2, 5), (6, 6)],
    5:  [(0, 5), (6, 7)],
    6:  [(0, 7), (7, 7)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 2, 2), (5, 0, 0), (6, 0, 0), (6, 7, 7)], "D"),
]
