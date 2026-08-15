"""Apex Mizutsune, mizutsune apex. The bubble dancer at full glory: crest
and tail fan grown one row taller with pink bubble clusters."""
from mizutsune import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-mizutsune"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["P"] = (228, 118, 152, 255)  # hot pink crest
CONFIG["palette"]["F"] = (216, 100, 150, 255)  # deep pink fan

# crest and fan grown even taller than the parent's
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(2, 7), (14, 15)],
    3:  [(1, 7), (14, 15)],
    4:  [(1, 7), (17, 18)],
    5:  [(1, 7), (10, 26), (29, 32)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # pink bubble clusters on the neck and flank
    ("runs", [(7, 8, 9), (10, 8, 9)], "F", "W"),
]
