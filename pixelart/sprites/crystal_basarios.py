"""Crystal Basarios, basarios variant. Ice-blue crystal rock over the
sleeping boulder frame."""
from basarios import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "crystal-basarios"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (150, 172, 198, 255)  # crystal rock
CONFIG["palette"]["D"] = (114, 136, 164, 255)  # darker crystal
CONFIG["palette"]["C"] = (204, 222, 240, 255)  # pale ice face
