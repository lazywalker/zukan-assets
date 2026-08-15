"""Porkeplume, bird wyvern. The pink plume pig: gargwa's plump bird frame
in rosy plumage with a head tuft and a curled tail nub."""
from gargwa import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "porkeplume"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (214, 142, 150, 255)  # rosy plumage
CONFIG["palette"]["D"] = (178, 108, 118, 255)  # darker rose
CONFIG["palette"]["C"] = (238, 212, 208, 255)  # pale face
CONFIG["palette"]["Y"] = (232, 170, 90, 255)   # warm beak / legs

# head tuft
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(8, 9)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(3, 8, 9)], "D"),
]
