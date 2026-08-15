"""Apex Zinogre, fanged wyvern. The thunder emperor at full charge: crown
and back spikes burst one row taller with lightning-gold tips, over the
zinogre frame in a deeper gold-white coat."""
from zinogre import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-zinogre"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (140, 190, 178, 255)  # pale storm fur
CONFIG["palette"]["G"] = (248, 208, 70, 255)   # bright storm gold
CONFIG["palette"]["g"] = (196, 150, 44, 255)   # dark gold

# crown + back spikes bursting one row taller
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(4, 5), (15, 15), (19, 19)],
    2:  [(4, 6), (15, 15), (19, 19), (28, 29)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # storm gold on the new spike tips
    ("runs", [(1, 4, 5), (1, 15, 15), (1, 19, 19)], "G"),
]
