"""Raging Brachydios, brachydios deviant. The eruption: both slime fists
bursting with extra glow blobs, slime bursting off the shoulder, over the
brachydios frame in a hotter red-navy coat."""
from brachydios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "raging-brachydios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["N"] = (76, 52, 96, 255)     # hot purple-navy body
CONFIG["palette"]["D"] = (54, 36, 70, 255)     # darker shade
CONFIG["palette"]["E"] = (232, 168, 84, 255)   # magma-orange slime
CONFIG["palette"]["e"] = (184, 116, 52, 255)   # dark slime

# slime bursts: blobs over the fist and the shoulder
CONFIG["spans"] = {
    **_base["spans"],
    7:  [(0, 8), (9, 14), (11, 11)],
    8:  [(0, 0), (1, 7), (9, 16)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # slime color on the burst blobs
    ("runs", [(7, 11, 11), (8, 0, 0)], "E"),
]
