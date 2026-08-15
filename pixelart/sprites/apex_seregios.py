"""Apex Seregios, seregios apex. The bloodied blade storm: deeper gold
over the seregios frame with red-tipped scales everywhere."""
from seregios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "apex-seregios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (196, 142, 56, 255)   # deeper gold
CONFIG["palette"]["D"] = (148, 102, 40, 255)   # darker gold
CONFIG["palette"]["R"] = (222, 62, 48, 255)    # blood-red tips
CONFIG["palette"]["C"] = (228, 186, 140, 255)  # warm chest

# the blade storm: taller crest spires and blood on the crest
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(5, 5), (9, 9)],
    2:  [(4, 10), (14, 15), (19, 20)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    # the taller crest spires and shoulder blades stand red
    ("runs", [(1, 5, 5), (1, 9, 9), (2, 4, 10)], "D"),
    ("put", 1, 5, "R"),
    ("put", 1, 9, "R"),
]
