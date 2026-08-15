"""Soulseer Mizutsune, mizutsune subspecies. The blind seer: pearl-white
scales over the bubble fox frame, the eyes closed seams, and pale blue
bubbles."""
from mizutsune import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "soulseer-mizutsune"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (232, 234, 240, 255)  # pearl-white body
CONFIG["palette"]["P"] = (168, 176, 200, 255)  # slate-blue crest
CONFIG["palette"]["F"] = (150, 158, 186, 255)  # slate-blue fan
CONFIG["palette"]["C"] = (196, 216, 232, 255)  # pale blue bubbles

# blind seer: crest droops short, fan held low
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(4, 6), (14, 15)],
    4:  [(2, 6), (17, 18)],
    10: [(0, 41)],
}

CONFIG["fills"] = [
    op for op in _base["fills"] if not (op[0] == "put" and op[1] == 8)
] + [
    # closed eyes: slate seam lines instead of the dark eye
    ("put", 8, 2, "PP"),
]
