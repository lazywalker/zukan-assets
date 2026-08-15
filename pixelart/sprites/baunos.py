"""Baunos, wingdrake. The lava snapper: noios' wingdrake frame in ember
red with a tall blazing double crest, a long pointed snout, and a pale
hot chest. The blazing crest is what separates it from mernos/noios."""
from noios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "baunos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["T"] = (172, 82, 58, 255)    # ember red body
CONFIG["palette"]["D"] = (136, 60, 44, 255)    # darker red
CONFIG["palette"]["B"] = (204, 128, 88, 255)   # warm wing
CONFIG["palette"]["R"] = (244, 160, 64, 255)   # hot orange crest
CONFIG["palette"]["Y"] = (250, 210, 110, 255)  # blazing crest tips

# tall double crest feathers + long pointed snout
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(4, 5), (8, 9)],
    2:  [(3, 6), (7, 10)],
    5:  [(1, 9), (7, 16)],
    6:  [(0, 10), (6, 18)],
    7:  [(1, 11), (5, 20)],
}

CONFIG["fills"] = [
    op for op in _base["fills"]
    if not (op[0] == "runs" and op[1][0] == (2, 5, 6))
] + [
    # blazing crest: hot orange with yellow tips
    ("runs", [(1, 4, 5), (1, 8, 9), (2, 3, 6), (2, 7, 10)], "R"),
    ("put", 1, 4, "Y"),
    ("put", 1, 8, "Y"),
    # snout tip shading
    ("runs", [(5, 1, 2), (6, 0, 1)], "D", "T"),
]
