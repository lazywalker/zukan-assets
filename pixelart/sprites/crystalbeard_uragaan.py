"""Crystalbeard Uragaan, uragaan subspecies. Crystal growths: pale shards
bristling from the boulder top and a heavy crystal beard merging into the
chin axe, over the uragaan frame in bluish plate."""
from uragaan import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "crystalbeard-uragaan"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (108, 118, 148, 255)  # bluish plate body
CONFIG["palette"]["D"] = (78, 88, 118, 255)    # darker shade
CONFIG["palette"]["C"] = (196, 226, 238, 255)  # ice-crystal beard
CONFIG["palette"]["Y"] = (226, 244, 250, 255)  # crystal glints

# crystal shards on the boulder top, beard row widened
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(14, 14), (16, 17), (19, 19)],
    13: [(1, 32)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # crystal color flooding the beard row
    ("runs", [(13, 1, 32)], "C", "E"),
    ("runs", [(1, 14, 14), (1, 16, 16), (1, 19, 19)], "Y", "B"),
]
