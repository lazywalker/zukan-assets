"""Great Wroggi, bird wyvern leader. Poison-dog variant of the
great-jaggi family: rose-red scales, a raised curled tail, a closed
muzzle, and the signature orange poison sacs glowing on the neck, flank
and tail base. Differs from jaggi by the raised tail and the sacs."""
from great_jaggi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-wroggi"
CONFIG["compare_to"] = "../icons/mh3u/great-wroggi.png"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (205, 105, 105, 255)  # rose scales
CONFIG["palette"]["F"] = (180, 80, 80, 255)    # dark rose frill
CONFIG["palette"]["C"] = (235, 185, 175, 255)  # pale underbelly
CONFIG["palette"]["S"] = (150, 65, 60, 255)    # spots / shade

# raised curled tail: tip lifted two rows above the jaggi pose
CONFIG["spans"] = {
    **_base["spans"],
    5:  [(5, 12), (30, 32)],
    6:  [(1, 12), (29, 33)],
    7:  [(1, 12), (29, 33)],
    8:  [(2, 11), (28, 33)],
    9:  [(3, 12), (13, 25), (28, 32)],
    10: [(5, 13), (14, 26), (28, 31)],
}

CONFIG["fills"] = [
    # rose frill behind the jaw
    ("runs", [(3, 8, 10), (4, 7, 11), (5, 10, 12)], "F"),
    # closed muzzle: cream beak, no mouth line
    ("runs", [(6, 1, 3), (7, 1, 3)], "C"),
    # eye
    ("put", 7, 5, "W"),
    # orange poison sacs: neck, flank, tail base
    ("runs", [(10, 7, 9), (11, 8, 10), (12, 8, 9), (13, 22, 24),
              (14, 23, 25)], "O"),
    # cream underbelly
    ("runs", [(13, 8, 12), (14, 8, 12), (15, 9, 12), (16, 10, 12)],
     "C"),
    # frill spikes along the raised tail top edge
    ("runs", [(6, 30, 31), (7, 31, 32), (8, 31, 32)], "F"),
    # tail underside shade
    ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
     "S"),
    # claws
    ("put", 21, 10, "W"),
    ("put", 21, 12, "W"),
    ("put", 21, 18, "W"),
    ("put", 21, 20, "W"),
]
