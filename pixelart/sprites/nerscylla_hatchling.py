"""Nerscylla Hatchling, temnoceran. A tiny nerscylla: the hood, red eyes
and fangs shrunk onto a small round body with stubby leg nubs."""
from nerscylla import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "nerscylla-hatchling"
CONFIG["compare_to"] = ""
CONFIG["size"] = (20, 24)
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["C"] = (220, 210, 190, 255)  # brighter pale body

CONFIG["spans"] = {
    2:  [(8, 11)],                           # abdomen top
    3:  [(7, 12)],
    4:  [(3, 4), (6, 13), (15, 16)],         # leg nubs
    5:  [(3, 4), (6, 13), (15, 16)],
    6:  [(6, 13)],
    7:  [(2, 3), (6, 13), (16, 17)],
    8:  [(2, 3), (6, 13), (16, 17)],
    9:  [(6, 13)],
    10: [(7, 12)],
    11: [(7, 12)],
    12: [(7, 12)],
    13: [(8, 11)],
    14: [(8, 11)],
    15: [(8, 11)],
    16: [(9, 10)],
}

CONFIG["fills"] = [
    # dark hood marking over the round abdomen
    ("runs", [(2, 8, 11), (3, 7, 9), (3, 10, 12), (4, 6, 8), (4, 11, 13),
              (5, 6, 8), (5, 11, 13), (6, 6, 7), (6, 12, 13), (7, 6, 7),
              (7, 12, 13), (8, 6, 7), (8, 12, 13), (9, 7, 8), (9, 11, 12)],
     "D", "C"),
    # purple hood band and head
    ("runs", [(10, 7, 12), (11, 7, 12), (12, 7, 12), (13, 8, 11),
              (14, 8, 11), (15, 8, 11)], "P", "C"),
    ("runs", [(10, 9, 10)], "D", "P"),
    # red eyes
    ("put", 13, 8, "R"),
    ("put", 13, 11, "R"),
    # white fangs below the head
    ("put", 16, 8, "W"),
    ("put", 16, 11, "W"),
    # purple leg nubs with dark tips
    ("runs", [(4, 3, 4), (5, 3, 4), (7, 2, 3), (8, 2, 3), (4, 15, 16),
              (5, 15, 16), (7, 16, 17), (8, 16, 17)], "P"),
    ("runs", [(5, 4, 4), (8, 3, 3), (5, 15, 15), (8, 16, 16)], "D", "P"),
]
