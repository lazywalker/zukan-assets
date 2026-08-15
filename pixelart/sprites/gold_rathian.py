"""Gold Rathian: the gleaming variant. Golden body and the tail held high
as a horizontal blade instead of drooping below the wing."""
from rathian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gold-rathian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (205, 168, 62, 255)
CONFIG["palette"]["D"] = (152, 120, 42, 255)

# raised tail: blade sweeps right at mid-height, droop tip removed
CONFIG["spans"] = {
    **_base["spans"],
    12: [(5, 17), (19, 19), (21, 21), (23, 23), (25, 26)],
    13: [(6, 17), (18, 27)],
    14: [(7, 17), (18, 27)],
    15: [(7, 17), (18, 25)],
    16: [(8, 16)],
    17: [(9, 11), (13, 15)],
    18: [(9, 11), (13, 15)],
}

CONFIG["fills"] = [
    op for op in _base["fills"]
    if not (op[0] == "put" and op[1] in (15, 16) and op[2] in (19, 18))
] + [
    # shade along the raised tail underside
    ("runs", [(14, 24, 27), (15, 23, 25), (12, 25, 26)], "D"),
]
