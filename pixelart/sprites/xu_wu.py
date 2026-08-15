"""Xu Wu, cephalopod. The helm squid: a big dark dome mantle with yellow
shards, tentacle arms curled tight at both sides, pale threads hanging
from the beak below."""
from nu_udra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "xu-wu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (62, 62, 66, 255)     # dark dome mantle
CONFIG["palette"]["D"] = (44, 44, 50, 255)     # darker shade
CONFIG["palette"]["Y"] = (216, 196, 84, 255)   # yellow shards
CONFIG["palette"]["P"] = (110, 140, 208, 255)  # blue arm accents

# dome mantle, arms curled at both sides, threads below
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(5, 6), (10, 11)],
    4:  [(3, 13)],
    5:  [(2, 14)],
    6:  [(1, 15)],
    7:  [(1, 16)],
    8:  [(0, 16)],
    9:  [(0, 16), (17, 18)],
    10: [(1, 15), (17, 20)],
    11: [(1, 14), (16, 21)],
    12: [(2, 13), (0, 0), (15, 22), (16, 16)],
    13: [(2, 12), (0, 0), (15, 23), (17, 17)],
    14: [(3, 11), (16, 23)],
    15: [(4, 10), (17, 22)],
    16: [(5, 9), (18, 21)],
    17: [(6, 8), (19, 20)],
}

CONFIG["fills"] = [
    # yellow shards scattered over the dome
    ("runs", [(5, 4, 5), (5, 9, 10), (6, 3, 3), (6, 12, 12),
              (7, 5, 6), (7, 10, 11), (8, 3, 3), (8, 13, 14),
              (9, 7, 8), (9, 12, 12), (10, 5, 5), (10, 10, 11),
              (11, 8, 8)], "Y"),
    # eye band
    ("runs", [(8, 6, 8), (8, 10, 11)], "P"),
    # curled arm accents
    ("runs", [(10, 17, 20), (11, 16, 21), (12, 15, 22)], "P", "O"),
    ("runs", [(12, 0, 0), (13, 0, 0)], "P"),
    # pale threads below the beak
    ("runs", [(13, 7, 8), (14, 7, 8)], "W"),
    # dome shade
    ("runs", [(7, 12, 16), (8, 14, 16), (9, 14, 16)], "D"),
]
