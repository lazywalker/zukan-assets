"""Desert Seltas Queen, seltas-queen subspecies. Sand-yellow tank armor
over the queen frame with a pale dune shell."""
from seltas_queen import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "desert-seltas-queen"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (188, 160, 92, 255)   # sand-yellow armor
CONFIG["palette"]["D"] = (148, 122, 66, 255)   # darker sand
CONFIG["palette"]["Y"] = (236, 206, 110, 255)  # pale horn tips
