"""Thunderlord Zinogre, fanged wyvern deviant. Twin horn-ear spikes split
from the crown, and the tail tip carries a lightning fork. Zinogre derive
with a deeper teal storm coat."""
from zinogre import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "thunderlord-zinogre"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (58, 148, 132, 255)   # deeper storm teal
CONFIG["palette"]["G"] = (250, 214, 92, 255)   # brighter gold
CONFIG["palette"]["V"] = (92, 140, 220, 255)   # lightning-blue claws

# twin horn-ear tips split from the crown
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(4, 4), (6, 6)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # gold on the horn-ear tips
    ("runs", [(1, 4, 4), (1, 6, 6)], "G"),
]
