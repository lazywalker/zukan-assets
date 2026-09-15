"""King marlin: a deep-blue billfish with a long spear bill at the front
and a tall sail dorsal fin."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "king-marlin"
CONFIG["size"] = (36, 24)
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (60, 92, 152, 255)    # blue body
CONFIG["palette"]["D"] = (40, 66, 120, 255)    # darker fins
CONFIG["palette"]["C"] = (202, 212, 226, 255)  # silver belly

CONFIG["spans"] = {
    **_base["spans"],
    5: [(9, 20)],
    6: [(8, 19)],
    9: [(0, 21), (20, 29)],
    10: [(0, 21), (20, 29)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the long spear bill
    ("runs", [(9, 0, 3), (10, 0, 3)], "C"),
    ("put", 9, 0, "D"),
    # tall sail dorsal
    ("runs", [(5, 9, 20), (6, 8, 19)], "D"),
]
