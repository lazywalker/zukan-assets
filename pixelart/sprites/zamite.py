"""Zamite, amphibian. The shark pup: a tiny zamtrios, fin and all, over
the shark-toad frame shrunk to a small round body."""
from zamtrios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "zamite"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (128, 164, 192, 255)  # pup blue

# small round body: clipped low and short
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(12, 23)],
    4:  [(10, 25), (23, 27)],
    5:  [(8, 26), (22, 28)],
    6:  [(6, 27), (21, 28)],
    7:  [(4, 27), (19, 29)],
    8:  [(2, 27), (18, 29)],
    9:  [(1, 27), (17, 30)],
    10: [(0, 27), (16, 30)],
    11: [(0, 27), (16, 30)],
    12: [(0, 26), (16, 30)],
    13: [(1, 26), (16, 29)],
    14: [(2, 25), (17, 29)],
    15: [(3, 24), (18, 28)],
    16: [(4, 22), (19, 27)],
    17: [(6, 20), (20, 26)],
    18: [(8, 11), (14, 17), (21, 25)],
}
