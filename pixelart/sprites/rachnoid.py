"""Rachnoid, temnoceran. A tiny rakna-kadaki: same crown and splayed legs
on a small pale body."""
from rakna_kadaki import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rachnoid"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["Y"] = (226, 214, 172, 255)  # brighter pale body

# small round body
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(5, 11), (12, 13)],
    4:  [(4, 12), (12, 15)],
    5:  [(3, 13), (11, 16)],
    6:  [(3, 14), (10, 17)],
    7:  [(2, 14), (9, 18)],
    8:  [(2, 15), (9, 19)],
    9:  [(2, 15), (9, 19)],
    10: [(2, 15), (9, 19)],
    11: [(2, 15), (9, 18)],
    12: [(2, 14), (10, 18)],
    13: [(3, 13), (11, 16)],
    14: [(3, 12), (12, 15)],
    15: [(4, 11), (13, 14)],
    16: [(5, 10)],
    17: [(5, 6), (8, 10)],
    18: [(4, 4), (6, 6), (8, 8), (10, 10)],
}
CONFIG["fills"] = [
    op for op in _base["fills"]
    if not (op[0] == "put" and op[1] == 18)
] + [
    ("put", 18, 4, "O"),
    ("put", 18, 6, "O"),
    ("put", 18, 8, "O"),
    ("put", 18, 10, "O"),
]
