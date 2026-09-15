"""The prism spiritbird: iridescent violet plumage."""
from _songbird import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "prism-spiritbird"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (160, 120, 190, 255)
CONFIG["palette"]["D"] = (118, 86, 146, 255)
CONFIG["palette"]["C"] = (226, 186, 250, 255)
