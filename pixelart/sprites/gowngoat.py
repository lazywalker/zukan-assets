"""Gowngoat, herbivore. The white grazer: kelbi's slender frame in a
shaggy white coat, curled dark horns, a chin beard, and fluff bumps on
the back."""
from kelbi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gowngoat"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (226, 222, 212, 255)  # shaggy white coat
CONFIG["palette"]["D"] = (186, 182, 172, 255)  # fluff shade
CONFIG["palette"]["G"] = (110, 100, 92, 255)   # dark curled horns

# beard + back fluff bumps
CONFIG["spans"] = {
    **_base["spans"],
    7:  [(3, 9), (11, 11), (14, 14)],
    9:  [(1, 9), (10, 17)],
}

CONFIG["fills"] = [
    # curled dark horns
    ("runs", [(3, 8, 10), (4, 7, 12), (5, 6, 13), (6, 11, 14),
              (7, 11, 15)], "G"),
    # face
    ("put", 6, 5, "K"),
    ("put", 7, 4, "D"),
    # beard + fluff bumps
    ("runs", [(7, 11, 11), (7, 14, 14), (9, 1, 1)], "D"),
    # belly shade
    ("runs", [(11, 4, 10), (12, 4, 12), (13, 5, 12), (14, 6, 11),
              (15, 7, 10)], "D"),
    # back shade
    ("runs", [(9, 12, 16), (10, 13, 17), (11, 13, 17)], "D"),
    # hooves
    ("put", 18, 7, "G"),
    ("put", 18, 9, "G"),
    ("put", 18, 13, "G"),
]
