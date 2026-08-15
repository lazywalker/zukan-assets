"""Chramine, bird wyvern. The cloud rooster: qurupeco's songbird frame in
a pale green coat with a warm ochre head, a puffed cream throat pouch,
and a wide flat tail fan."""
from qurupeco import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "chramine"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (156, 172, 132, 255)  # green plumage
CONFIG["palette"]["D"] = (118, 134, 96, 255)   # darker green
CONFIG["palette"]["R"] = (198, 142, 62, 255)   # warm ochre head
CONFIG["palette"]["F"] = (228, 208, 150, 255)  # cream pouch
CONFIG["palette"]["P"] = (128, 140, 108, 255)  # sage tail

# puffier throat pouch + wider flat tail fan
CONFIG["spans"] = {
    **_base["spans"],
    8:  [(0, 9), (9, 21)],
    9:  [(0, 9), (8, 22)],
    10: [(1, 9), (8, 23)],
    4:  [(3, 7), (12, 16)],
    5:  [(2, 8), (11, 18)],
}
