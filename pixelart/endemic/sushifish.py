"""Sushifish: the fish that looks like sushi; white body with a red-orange
back band and a dark tail, like tuna on rice."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "sushifish"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (240, 234, 222, 255)  # rice-white body
CONFIG["palette"]["D"] = (150, 62, 44, 255)    # dark tail
CONFIG["palette"]["C"] = (248, 242, 230, 255)  # pale belly
CONFIG["palette"]["R"] = (208, 84, 48, 255)    # salmon-red topping

CONFIG["fills"] = list(_base["fills"]) + [
    # red-orange topping band across the back
    ("runs", [(8, 5, 19), (9, 4, 19), (10, 4, 19), (11, 4, 20),
              (12, 4, 20), (13, 5, 19)], "R", "B"),
]
