"""Jade Barroth, barroth subspecies. Snow-clay crown: pale ice-blue body
with a spikier white crown, over the same hammerhead frame."""
from barroth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "jade-barroth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (128, 148, 152, 255)  # ice-blue body
CONFIG["palette"]["D"] = (96, 114, 120, 255)   # darker shade
CONFIG["palette"]["O"] = (226, 232, 236, 255)  # white snow crown
CONFIG["palette"]["S"] = (170, 186, 192, 255)  # crown notch lines
CONFIG["palette"]["L"] = (168, 184, 190, 255)  # icy belly band

# spikier snow crown: bumps above the ridge
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(4, 5), (7, 8)],
}
