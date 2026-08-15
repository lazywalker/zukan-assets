"""Rafma, small herbivore. The ice floe scurrier: jagras' little frame in
a pale ice-blue coat with white ear tufts, a frost-white belly, and
frost spikes instead of yellow."""
from jagras import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rafma"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (172, 182, 192, 255)  # pale ice-blue scales
CONFIG["palette"]["D"] = (136, 146, 158, 255)  # darker bands
CONFIG["palette"]["Y"] = (236, 242, 246, 255)  # frost spikes / stripes
CONFIG["palette"]["O"] = (206, 214, 222, 255)  # frost belly

# white ear tufts
CONFIG["spans"] = {
    **_base["spans"],
    4:  [(2, 2), (5, 5)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(4, 2, 2), (4, 5, 5)], "Y"),
]
