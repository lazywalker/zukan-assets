"""Stygian Zinogre: the crimson-spiked variant. Black body, and the shell
growth is fiercer: crown spike one row taller and two extra back spikes
between the gold ridge rows."""
from zinogre import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "stygian-zinogre"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (62, 62, 74, 255)
CONFIG["palette"]["t"] = (42, 42, 52, 255)
CONFIG["palette"]["G"] = (196, 62, 52, 255)
CONFIG["palette"]["g"] = (142, 40, 36, 255)

# fiercer shell: taller crown tip + extra back spikes
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(4, 5)],
    2:  [(4, 6), (15, 15), (19, 19), (28, 29)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # crimson shell on the new spikes
    ("runs", [(1, 4, 5), (2, 15, 15), (2, 19, 19)], "G"),
]
