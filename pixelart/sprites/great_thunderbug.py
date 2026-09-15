"""Great Thunderbug, neopteron. The storm bulb: vespoid's frame swollen
into a round glowing blue body on small dangling legs, with bright
shimmer glints."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-thunderbug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (246, 242, 230, 255)   # white belly / glints
CONFIG["palette"]["R"] = (94, 128, 198, 255)   # storm blue body
CONFIG["palette"]["Y"] = (180, 216, 246, 255)  # pale shimmer bands
CONFIG["palette"]["D"] = (64, 92, 156, 255)    # darker blue

# round bulb body on two small legs
CONFIG["spans"] = {
    **_base["spans"],
    10: [(3, 4), (8, 17), (21, 22)],
    11: [(8, 17)],
    12: [(6, 6), (8, 17), (19, 19)],
    13: [(6, 6), (8, 17), (19, 19)],
    14: [(8, 17)],
    15: [(8, 17)],
    16: [(9, 16)],
    17: [(10, 15)],
    18: [(11, 14)],
}

# drop the parent leg fills that now run inside the bulb, keep the rest
CONFIG["fills"] = [
    op for op in _base["fills"]
    if not (op[0] == "runs" and op[1][0][0] in (12, 13, 14)
            and op[1][0][1] in (6, 8))
    and not (op[0] == "put" and op[1] == 14 and op[2] in (6, 8, 17, 19))
] + [
    ("runs", [(12, 6, 6), (12, 19, 19), (13, 6, 6), (13, 19, 19)], "D"),
    # bright shimmer glints on the bulb
    ("put", 10, 10, "W"),
    ("put", 10, 15, "W"),
    ("put", 12, 9, "W"),
    ("put", 12, 16, "W"),
]
