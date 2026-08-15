"""One-Eared Yian Garuga, garuga variant. The torn veteran: yian-garuga's
crest with one side torn off and extra scars."""
from scarred_yian_garuga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "one-eared-yian-garuga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (232, 226, 214, 255)  # pale old spikes

# crest torn: right side missing
CONFIG["spans"] = {
    **_base["spans"],
    3:  [(5, 9)],
    4:  [(4, 10)],
}

CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(6, 8, 9), (7, 9, 10)], "C"),
]
