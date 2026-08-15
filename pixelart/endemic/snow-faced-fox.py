"""Snow-faced fox: the fox with a snow-white face patch over its eyes."""
from _fox import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "snow-faced-fox"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (176, 150, 120, 255)  # tan pelt
CONFIG["palette"]["D"] = (132, 108, 82, 255)   # darker

CONFIG["fills"] = list(_base["fills"]) + [
    # the snow-white face mask around the eyes
    ("runs", [(7, 5, 12), (8, 6, 12)], "C"),
    ("put", 8, 7, "K"),
]
