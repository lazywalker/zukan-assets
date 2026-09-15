"""Izuchi, small bird wyvern. The sickle head: a pale grey lunge frame
with a big scythe blade of bone sweeping back off the skull."""
from velocidrome import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "izuchi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (246, 242, 230, 255)   # white belly / glints
CONFIG["palette"]["O"] = (172, 174, 168, 255)  # pale grey scales
CONFIG["palette"]["F"] = (206, 208, 202, 255)  # pale crest
CONFIG["palette"]["C"] = (216, 218, 212, 255)  # pale belly
CONFIG["palette"]["S"] = (120, 122, 116, 255)  # dark spots

# scythe blade sweeping back off the skull
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(8, 12)],
    3:  [(7, 13)],
    4:  [(6, 12)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # bone blade, pale with a sharp tip
    ("runs", [(2, 8, 12), (3, 7, 13), (4, 6, 12)], "F"),
    ("put", 2, 11, "W"),
    ("put", 2, 12, "W"),
]
