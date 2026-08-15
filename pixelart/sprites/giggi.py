"""Giggi, flying wyvern. A tiny gigginox: same pale crest and twin tail
heads on a small flat body."""
from gigginox import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "giggi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (168, 108, 118, 255)  # brighter pup body

# small flat body
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(3, 10), (11, 12)],
    7:  [(2, 11), (10, 14)],
    8:  [(2, 12), (9, 16)],
    9:  [(1, 12), (9, 18)],
    10: [(1, 12), (9, 19)],
    11: [(1, 12), (9, 19)],
    12: [(1, 12), (9, 19)],
    13: [(2, 12), (9, 19)],
    14: [(2, 12), (10, 20)],
    15: [(3, 12), (11, 20)],
    16: [(3, 12), (12, 20)],
    17: [(4, 11), (13, 20)],
    18: [(5, 11), (15, 19)],
    19: [(6, 10), (17, 18)],
    20: [(6, 9), (18, 18)],
}
