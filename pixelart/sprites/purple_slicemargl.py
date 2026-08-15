"""Purple Slicemargl, flying wyvern. The violet blade: seregios' blade
scale frame in deep violet with pale slicing edges."""
from seregios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "purple-slicemargl"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (128, 84, 148, 255)   # deep violet scales
CONFIG["palette"]["D"] = (96, 60, 114, 255)    # darker violet
CONFIG["palette"]["R"] = (226, 168, 216, 255)  # pale slicing edges
CONFIG["palette"]["C"] = (210, 178, 200, 255)  # pale chest

# the slicer: the tail ends in a long pale-edged razor blade
CONFIG["size"] = (36, 24)
CONFIG["spans"] = {
    **_base["spans"],
    5:  [(2, 12), (26, 33)],
    6:  [(1, 13), (25, 34)],
    7:  [(1, 13), (13, 24), (25, 30), (33, 34)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # pale slicing edge along the tail blade
    ("runs", [(5, 30, 33), (6, 31, 34), (7, 33, 34)], "R"),
]
