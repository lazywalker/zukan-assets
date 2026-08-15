"""Lala Barina, temnoceran. The rose dancer: a crimson body with a white
cross mark on the abdomen, a fluffy pink ruff at the waist, and thin
stilt legs. Slimmer and daintier than the widow."""
from rakna_kadaki import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "lala-barina"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["Y"] = (198, 76, 88, 255)    # crimson body
CONFIG["palette"]["D"] = (154, 54, 66, 255)    # darker crimson
CONFIG["palette"]["V"] = (238, 168, 186, 255)  # pink ruff
CONFIG["palette"]["O"] = (150, 104, 142, 255)  # mauve legs

# fluffy ruff at the waist
CONFIG["spans"] = {
    **_base["spans"],
    9:  [(0, 16), (7, 21)],
    10: [(0, 16), (7, 21)],
}

CONFIG["fills"] = [
    # dark crown low on the head
    ("runs", [(3, 4, 11), (4, 3, 12), (5, 2, 10), (6, 2, 8)], "D"),
    # pale eyes
    ("put", 5, 4, "W"),
    # white cross on the abdomen
    ("runs", [(10, 11, 14), (11, 12, 13), (12, 11, 14)], "W", "Y"),
    ("runs", [(11, 10, 10), (11, 15, 15)], "W", "Y"),
    # pink ruff at the waist
    ("runs", [(9, 0, 20), (10, 7, 20)], "V"),
    ("runs", [(9, 3, 3), (9, 8, 8), (9, 13, 13), (9, 17, 17),
              (10, 9, 9), (10, 14, 14), (10, 18, 18)], "D", "V"),
    # mauve legs
    ("runs", [(4, 12, 16), (5, 11, 17), (6, 10, 18)], "O"),
    ("runs", [(16, 12, 15), (17, 9, 11), (17, 13, 14)], "O"),
    ("put", 18, 4, "O"),
    ("put", 18, 6, "O"),
    ("put", 18, 8, "O"),
    ("put", 18, 12, "O"),
    ("put", 18, 14, "O"),
]
