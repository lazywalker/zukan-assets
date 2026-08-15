"""Jaggia, small bird wyvern. The brown pack female: jaggi's frame in a
dull brown coat, crest dropped low, pale neck bands."""
from jaggi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "jaggia"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (150, 116, 84, 255)   # dull brown scales
CONFIG["palette"]["F"] = (176, 142, 104, 255)  # pale crest
CONFIG["palette"]["S"] = (114, 86, 60, 255)    # dark spots

# crest dropped low, one row shorter
CONFIG["spans"] = {
    **_base["spans"],
    3:  [],
    4:  [(7, 11)],
}
