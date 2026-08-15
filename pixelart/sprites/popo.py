"""Popo, herbivore. The tundra tusker: anteka's stocky frame in a shaggier
grey coat, antlers reduced to short spikes, and a pale tusk pushing out
of the muzzle."""
from anteka import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "popo"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (158, 148, 138, 255)  # shaggy grey coat
CONFIG["palette"]["D"] = (122, 112, 104, 255)  # darker shade

# short spike antlers + tusk bump on the muzzle
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(5, 6), (11, 12)],
    2:  [(5, 7), (10, 13)],
    9:  [(0, 14), (6, 20)],
}

CONFIG["fills"] = [
    # dark spike antlers
    ("runs", [(1, 5, 6), (1, 11, 12), (2, 5, 7), (2, 10, 13),
              (3, 4, 9), (4, 8, 12)], "H"),
    # pale tusk
    ("runs", [(9, 0, 1)], "C"),
    # pale muzzle
    ("runs", [(7, 1, 3), (8, 1, 3)], "C"),
    # eye
    ("put", 6, 4, "K"),
    # pale belly band
    ("runs", [(13, 4, 14), (14, 5, 13), (15, 6, 12), (16, 7, 11)], "C"),
    # back shade
    ("runs", [(9, 12, 19), (10, 13, 20), (11, 14, 20)], "D"),
    # hooves
    ("put", 19, 7, "D"),
    ("put", 19, 9, "D"),
    ("put", 19, 13, "D"),
]
