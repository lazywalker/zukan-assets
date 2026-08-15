"""Gelidron, amphibian. The ice slug: slagtoth's droopy lump in frost
white with pale ice spikes along the back and a frozen breath drip."""
from slagtoth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "gelidron"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (196, 212, 224, 255)  # frost white hide
CONFIG["palette"]["D"] = (156, 176, 194, 255)  # darker ice
CONFIG["palette"]["M"] = (226, 238, 248, 255)  # pale ice spikes
CONFIG["palette"]["C"] = (222, 232, 240, 255)  # pale throat

# ice spikes along the back ridge
CONFIG["spans"] = {
    **_base["spans"],
    6:  [(4, 16), (17, 18), (20, 21)],
    7:  [(3, 18), (17, 22)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    ("runs", [(6, 17, 18), (6, 20, 21), (7, 17, 22)], "M"),
]
