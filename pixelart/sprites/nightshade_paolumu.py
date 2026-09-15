"""Nightshade Paolumu, paolumu subspecies. The alert variant: dark navy
fluff, pink face, glowing green eyes, and the ears flared one size
wider than the sleeping base's."""
from paolumu import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "nightshade-paolumu"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (100, 90, 122, 255)   # dark navy fluff
CONFIG["palette"]["C"] = (74, 66, 96, 255)     # darker fluff shade
CONFIG["palette"]["O"] = (225, 140, 160, 255)  # pink face / ears
CONFIG["palette"]["D"] = (150, 75, 105, 255)   # plum-pink shade
CONFIG["palette"]["P"] = (150, 75, 105, 255)   # plum-pink tail

# ears flared wider
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(5, 8), (19, 22)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # glowing green eyes
    ("put", 8, 12, "E"),
    ("put", 8, 15, "E"),
]
CONFIG["palette"]["E"] = (120, 205, 130, 255)  # glowing green eyes
