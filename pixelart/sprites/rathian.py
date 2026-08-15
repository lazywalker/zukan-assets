"""Rathian, side view: green female counterpart of rathalos. Palette swap
plus a span patch: the male's horn is replaced by a small crest nub.

Known simplification: a true rathian also differs in head breadth and the
tail spike arrangement; those need a head/tail part patch, not just spans
edits, and are deferred until the part mechanism exists.
"""
from rathalos import CONFIG as _base

HORN_OP = ("runs", [(1, 3, 3), (2, 2, 3), (3, 2, 4), (4, 2, 4), (10, 3, 5)],
           "C")
CREST_OP = ("runs", [(3, 3, 4), (10, 3, 5)], "C")

CONFIG = dict(_base)
CONFIG["name"] = "rathian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (104, 148, 66, 255)
CONFIG["palette"]["D"] = (60, 96, 40, 255)

CONFIG["spans"] = dict(_base["spans"])
CONFIG["spans"][1] = [(19, 21)]               # horn tip gone
CONFIG["spans"][2] = [(17, 23)]               # horn body gone
CONFIG["spans"][3] = [(3, 5), (15, 21)]       # small crest nub

CONFIG["fills"] = [CREST_OP if op == HORN_OP else op for op in _base["fills"]]
