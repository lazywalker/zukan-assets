"""Sea Lord's crestfish: a deep-sea fish with a tall jagged red crest
running along its back."""
from _fish import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "sealords-crestfish"
CONFIG["size"] = (36, 24)
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (56, 64, 100, 255)    # deep-sea body
CONFIG["palette"]["D"] = (38, 44, 74, 255)     # darker fins
CONFIG["palette"]["C"] = (160, 170, 205, 255)  # pale belly
CONFIG["palette"]["R"] = (206, 72, 56, 255)    # red crest

CONFIG["spans"] = {
    **_base["spans"],
    3: [(8, 9), (13, 14), (18, 19)],
    4: [(6, 10), (12, 15), (17, 20)],
    5: [(5, 21)],
}

CONFIG["fills"] = [
    op for op in _base["fills"] if not (op[0] == "runs" and op[1][0] == (6, 10, 17))
] + [
    # tall red crest spires
    ("runs", [(3, 8, 9), (3, 13, 14), (3, 18, 19), (4, 6, 10),
              (4, 12, 15), (4, 17, 20), (5, 5, 21)], "R"),
    # body stays dark blue with a pale belly
    ("runs", [(13, 6, 19), (14, 6, 18), (15, 7, 17), (16, 9, 16)], "C"),
]
