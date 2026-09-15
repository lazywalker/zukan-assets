"""Xu Wu, cephalopod. The helm squid: the octopus frame in near-black
slate, the flame crown turned to a dark spiked crest with gold shards,
arms curled tighter, and pale threads hanging from the beak."""
from nu_udra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "xu-wu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (48, 50, 58, 255)     # near-black slate mantle
CONFIG["palette"]["D"] = (34, 36, 44, 255)     # darker shade
CONFIG["palette"]["O"] = (62, 62, 66, 255)     # dark spiked crest
CONFIG["palette"]["T"] = (70, 80, 95, 255)     # dark arm stripes
CONFIG["palette"]["P"] = (110, 140, 208, 255)  # blue arm accents

# arms curled tighter than the parent, no tail tips
CONFIG["spans"] = {
    **_base["spans"],
    15: [(2, 4), (7, 10), (13, 20), (23, 26), (29, 31)],
    16: [(2, 4), (7, 10), (13, 20), (23, 26), (29, 31)],
    17: [(3, 5), (8, 11), (14, 19), (22, 24), (28, 30)],
    18: [(4, 6), (9, 11), (22, 24), (27, 29)],
    19: [],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # gold shards scattered over the mantle
    ("runs", [(5, 12, 13), (5, 20, 21), (6, 11, 11), (6, 22, 22),
              (7, 12, 13), (7, 20, 21), (9, 11, 11), (9, 22, 22),
              (10, 12, 13), (10, 20, 21)], "Y", "G"),
    # pale threads hanging from the beak
    ("runs", [(16, 15, 16), (16, 17, 18), (17, 16, 17)], "W", "G"),
]
