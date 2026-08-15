"""Brute Tigrex: the charcoal juggernaut. Bigger head with the jaw
reaching the frame edge, and no body stripes: plain dark plating with the
yellow bands kept only on the crown, tail and legs."""
from tigrex import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "brute-tigrex"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (76, 70, 64, 255)
CONFIG["palette"]["N"] = (228, 190, 52, 255)

# oversized head: snout and jaw push forward to col 0
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(0, 13), (25, 31)],
    7:  [(0, 13), (13, 24), (25, 30)],
    8:  [(1, 13), (13, 25), (25, 28)],
}

CONFIG["fills"] = [
    # yellow crown ridge over the skull top
    ("runs", [(2, 4, 8), (3, 3, 10), (4, 2, 11)], "N"),
    # neck band behind the eye
    ("runs", [(5, 11, 12), (6, 11, 13), (7, 11, 13)], "N"),
    # tail bands
    ("runs", [(2, 29, 30), (3, 28, 30), (4, 27, 30), (5, 26, 30),
              (6, 25, 28)], "N"),
    # cream lower jaw + chin, extended with the head
    ("runs", [(9, 2, 12), (10, 2, 11), (11, 3, 11)], "M"),
    # cream belly
    ("runs", [(12, 12, 19), (13, 12, 19), (14, 13, 18), (15, 13, 18)], "M"),
    # leg stripe bands
    ("runs", [(17, 15, 17), (18, 15, 17), (17, 23, 25), (18, 23, 25)], "N"),
    # eye + fangs + teeth
    ("put", 6, 4, "CK"),
    ("put", 7, 2, "W"),
    ("put", 7, 4, "W"),
    ("put", 8, 3, "W"),
    # claws
    ("put", 21, 13, "V"),
    ("put", 21, 15, "V"),
    ("put", 21, 22, "V"),
    ("put", 21, 24, "V"),
]
