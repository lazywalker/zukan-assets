"""Nightshade Paolumu, paolumu subspecies. The alert variant: dark navy
fluff, pink face, glowing green eyes, and the wing arms flapped one row
higher than the sleeping base's."""
from paolumu import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "nightshade-paolumu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (100, 90, 122, 255)   # dark navy fluff
CONFIG["palette"]["g"] = (74, 66, 96, 255)     # darker wing arms / flecks
CONFIG["palette"]["O"] = (225, 140, 160, 255)  # pink face / ear / pads
CONFIG["palette"]["P"] = (150, 75, 105, 255)   # plum-pink tail
CONFIG["palette"]["E"] = (120, 205, 130, 255)  # glowing green eyes

# wings flapped up: arm tips one row higher
CONFIG["spans"] = {
    **_base["spans"],
    0:  [(2, 3), (24, 25)],
    1:  [(1, 4), (23, 26)],
    2:  [(1, 5), (22, 26)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # glowing green eyes
    ("put", 11, 12, "E"),
    ("put", 12, 12, "E"),
    ("put", 11, 15, "E"),
    ("put", 12, 15, "E"),
]
