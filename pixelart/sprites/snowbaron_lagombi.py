"""Snowbaron Lagombi, lagombi deviant. The snow-chunker: lagombi's frame
in a whiter winter coat with blue ice patches and a snow boulder in the
paws."""
from lagombi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "snowbaron-lagombi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (238, 236, 230, 255)  # whiter winter fur
CONFIG["palette"]["D"] = (204, 200, 192, 255)  # lighter shade
CONFIG["palette"]["P"] = (150, 178, 208, 255)  # ice-blue patches

# snow boulder in the paws
CONFIG["spans"] = {
    **_base["spans"],
    14: [(5, 22), (10, 13)],
    15: [(5, 22), (9, 14)],
    16: [(6, 22), (10, 13)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(14, 10, 13), (15, 9, 14), (16, 10, 13)], "P"),
    ("put", 15, 11, "W"),
]
