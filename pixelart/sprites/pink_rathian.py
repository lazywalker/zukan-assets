"""Pink Rathian: the thorn queen. Magenta-pink body plus a spiked crown
on the head and thorn bumps along the back, on top of the rathian
crest-nub frame."""
from rathian import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "pink-rathian"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (190, 100, 150, 255)
CONFIG["palette"]["D"] = (130, 60, 105, 255)

# spiked crown + back thorns
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(19, 21), (2, 2), (5, 5)],
    2:  [(17, 23), (2, 3), (5, 6)],
    11: [(1, 4), (5, 10), (13, 13), (16, 16)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # dark thorns with pale tips on the crown
    ("runs", [(1, 2, 2), (1, 5, 5), (2, 2, 3), (2, 5, 6)], "D"),
    ("put", 1, 5, "W"),
    # back thorns
    ("runs", [(11, 13, 13), (11, 16, 16)], "D"),
    ("put", 11, 13, "W"),
    ("put", 11, 16, "W"),
]
