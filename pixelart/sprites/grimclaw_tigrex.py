"""Grimclaw Tigrex, tigrex deviant. The shadow brute: charcoal hide with
blood-red stripes over the tigrex frame, claws grown huge."""
from tigrex import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "grimclaw-tigrex"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (78, 70, 72, 255)     # charcoal hide
CONFIG["palette"]["N"] = (196, 62, 52, 255)    # blood-red stripes
CONFIG["palette"]["M"] = (216, 200, 176, 255)  # pale jaw
CONFIG["palette"]["C"] = (210, 62, 52, 255)    # red eye
CONFIG["palette"]["V"] = (30, 26, 28, 255)     # near-black claws

# claws grown huge
CONFIG["spans"] = {
    **_base["spans"],
    21: [(12, 13), (14, 16), (21, 23), (24, 26)],
}
