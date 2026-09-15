"""Risen Crimson Glow Valstrax, crimson-glow-valstrax variant. The
ascended comet: pearl-white body over the burning jet frame, exhaust
turned gold-white."""
from crimson_glow_valstrax import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "risen-crimson-glow-valstrax"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (236, 234, 238, 255)  # ascended pearl body
CONFIG["palette"]["D"] = (196, 194, 202, 255)  # darker pearl
CONFIG["palette"]["R"] = (232, 116, 76, 255)   # molten wings
CONFIG["palette"]["r"] = (252, 216, 150, 255)  # gold-white exhaust

# the wing stays pearl; only the trailing edge turns molten gold so the
# wing reads as a wing, not a second face
CONFIG["fills"] = [
    op for op in _base["fills"] if not (op[0] == "runs" and op[2] == "R")
] + [
    ("runs", [(4, 8, 13), (5, 7, 15), (6, 6, 17), (7, 5, 19),
              (8, 4, 21), (9, 4, 22), (10, 4, 23), (11, 4, 23)], "R"),
    ("runs", [(4, 10, 13), (5, 11, 15), (6, 12, 17), (7, 12, 19)],
     "D"),
    ("runs", [(8, 17, 21), (9, 18, 22), (10, 19, 23), (11, 19, 23),
              (12, 19, 23), (13, 19, 23), (14, 19, 23)], "r"),
]
