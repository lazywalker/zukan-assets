"""Crystalbeard Uragaan, uragaan subspecies. Crystal growths: pale shards
bristling from the boulder top and a heavy crystal beard under the chin
axe, over the uragaan frame in bluish plate."""
from uragaan import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "crystalbeard-uragaan"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (108, 118, 148, 255)  # bluish plate body
CONFIG["palette"]["D"] = (78, 88, 118, 255)    # darker shade
CONFIG["palette"]["C"] = (196, 226, 238, 255)  # ice-crystal beard
CONFIG["palette"]["O"] = (226, 244, 250, 255)  # crystal glints

# crystal shards on the boulder top + beard below the chin
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(13, 14), (19, 20)],
    13: [(0, 32)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # crystals on the top spikes and the beard
    ("runs", [(2, 13, 14), (2, 19, 20), (13, 0, 2)], "C"),
    ("runs", [(13, 0, 0), (2, 13, 13), (2, 19, 19)], "O", "C"),
]
