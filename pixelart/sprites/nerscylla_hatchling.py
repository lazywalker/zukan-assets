"""Nerscylla Hatchling, temnoceran. A tiny nerscylla: same hood and fangs
shrunk to a small round body."""
from nerscylla import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "nerscylla-hatchling"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["C"] = (220, 210, 190, 255)  # brighter pale body

# small round body
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(5, 11), (13, 13)],
    5:  [(4, 12), (13, 14)],
    6:  [(3, 13), (12, 15)],
    7:  [(3, 13), (11, 16)],
    8:  [(2, 14), (10, 17)],
    9:  [(2, 14), (10, 17)],
    10: [(2, 14), (10, 17)],
    11: [(2, 13), (10, 16)],
    12: [(2, 13), (11, 16)],
    13: [(3, 12), (12, 15)],
    14: [(3, 11), (13, 14)],
    15: [(4, 10), (14, 13)],
    16: [(5, 9)],
    17: [(5, 6), (8, 9)],
    18: [(5, 5), (7, 7), (9, 9)],
}
CONFIG["fills"] = [
    op for op in _base["fills"]
    if not (op[0] == "put" and op[1] == 18)
] + [
    ("put", 18, 5, "D"),
    ("put", 18, 7, "D"),
    ("put", 18, 9, "D"),
]
