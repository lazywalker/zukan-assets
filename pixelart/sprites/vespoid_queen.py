"""Vespoid Queen, neopteron. The queen wasp: a big vespoid with a crown
crest, longer abdomen, and brighter bands."""
from vespoid import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "vespoid-queen"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (188, 92, 66, 255)    # richer red body
CONFIG["palette"]["Y"] = (240, 196, 84, 255)   # brighter bands

# crown crest + longer abdomen
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(8, 9), (12, 13)],
    3:  [(7, 10), (12, 14)],
    13: [(3, 14), (13, 19)],
    14: [(3, 14), (14, 19)],
    15: [(4, 13), (15, 18)],
}
