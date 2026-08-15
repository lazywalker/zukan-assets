"""Larinoth, herbivore. The yellow giraffe: aptonoth's long neck stretched
one row taller with a green head plate and brown spots. Aptonoth derive."""
from aptonoth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "larinoth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (212, 182, 92, 255)   # yellow hide
CONFIG["palette"]["D"] = (172, 144, 66, 255)   # darker yellow
CONFIG["palette"]["V"] = (110, 162, 82, 255)   # green head plate / stripe

# neck stretched one row taller
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(2, 5)],
    2:  [(1, 6), (6, 7)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # green head plate over the crown
    ("runs", [(1, 2, 5), (2, 1, 6)], "V"),
    # brown spots on the body
    ("runs", [(11, 18, 19), (12, 20, 21), (13, 17, 18), (14, 21, 22)],
     "D"),
]
