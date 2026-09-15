"""Giant vigorwasp: the same lantern-and-wasp as its small cousin, but the
lantern is a level larger and the wasp is chunky."""
from _wasp import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "giant-vigorwasp"
CONFIG["size"] = (32, 24)

CONFIG["spans"] = {
    **_base["spans"],
    3: [(10, 12), (20, 21)],
    4: [(7, 23)],
    5: [(6, 24)],
    6: [(5, 25)],
    7: [(5, 25)],
    8: [(5, 24)],
    9: [(6, 23)],
    10: [(8, 20)],
    11: [(14, 14), (17, 17)],
    12: [(12, 20)],
    13: [(11, 21)],
    14: [(11, 21)],
    15: [(12, 20)],
    16: [(14, 18)],
    17: [(11, 11), (14, 14), (16, 16), (19, 19)],
}

CONFIG["fills"] = [
    op for op in _base["fills"]
    if not (op[0] == "put" and op[1:3] == (12, 10))
] + [
    # bright core ring
    ("runs", [(6, 12, 18), (7, 10, 12), (7, 18, 20)], "W"),
    ("put", 12, 13, "K"),
]
