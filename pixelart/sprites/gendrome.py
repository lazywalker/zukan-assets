"""Gendrome, bird wyvern leader. The paralyze-dog of the great-jaggi
family: yellow-green scales, the frill flared extra wide with pale tips,
two white fangs bared over the mouth line. Differs from jaggi by the
wide flaring frill and bared fangs."""
from great_jaggi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gendrome"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (200, 185, 80, 255)   # yellow scales
CONFIG["palette"]["F"] = (220, 200, 120, 255)  # yellow frill
CONFIG["palette"]["C"] = (225, 215, 150, 255)  # pale belly
CONFIG["palette"]["S"] = (145, 130, 50, 255)   # spots / shade

# extra wide flaring frill behind the jaw
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(6, 7), (12, 14)],
    3:  [(6, 14)],
    4:  [(5, 14)],
    5:  [(4, 13)],
}

CONFIG["fills"] = [
    # wide frill with pale flare tips
    ("runs", [(2, 6, 7), (2, 12, 14), (3, 6, 14), (4, 5, 14),
              (5, 10, 13)], "F"),
    ("put", 2, 6, "C"),
    ("put", 2, 14, "C"),
    # beak: cream
    ("runs", [(6, 1, 3), (7, 1, 3)], "C"),
    # dark mouth line
    ("runs", [(8, 2, 3)], "S"),
    # bared fangs over the mouth line
    ("put", 8, 2, "W"),
    ("put", 8, 5, "W"),
    # eye
    ("put", 7, 5, "W"),
    # dark spots on the body
    ("runs", [(11, 17, 18), (12, 19, 20), (13, 21, 22), (14, 12, 13),
              (14, 23, 24)], "S"),
    # cream underbelly
    ("runs", [(13, 8, 12), (14, 8, 12), (15, 9, 12), (16, 10, 12)],
     "C"),
    # frill spikes on the tail top
    ("runs", [(9, 24, 25), (10, 26, 27), (11, 27, 28)], "F"),
    # tail underside shade
    ("runs", [(13, 24, 29), (14, 24, 29), (15, 25, 28), (16, 24, 26)],
     "S"),
    # claws
    ("put", 21, 10, "W"),
    ("put", 21, 12, "W"),
    ("put", 21, 18, "W"),
    ("put", 21, 20, "W"),
]
