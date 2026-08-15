"""Ancient Leshen, leshen variant. The elder root: a darker bark body with
amber runes over the leshen frame and heavier antlers."""
from leshen import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ancient-leshen"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (52, 44, 44, 255)     # darker ancient bark
CONFIG["palette"]["D"] = (38, 32, 32, 255)     # darkest bark
CONFIG["palette"]["T"] = (124, 96, 66, 255)    # weathered antlers
CONFIG["palette"]["G"] = (232, 176, 92, 255)   # amber runes

# the elder root: a third antler tine and a mossy shoulder
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(2, 2), (4, 4), (9, 9)],
    2:  [(2, 5), (8, 10)],
    10: [(2, 12), (12, 12), (13, 17)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the extra tine + moss tuft on the shoulder
    ("runs", [(1, 2, 2), (2, 2, 2)], "T"),
    ("runs", [(10, 11, 12), (11, 12, 13)], "G"),
]
