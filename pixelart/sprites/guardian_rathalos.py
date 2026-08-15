"""Guardian Rathalos, rathalos variant. The constructed king: milky white
scales over the rathalos frame with an amber membrane sheen."""
from rathalos import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "guardian-rathalos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (220, 218, 212, 255)  # milky white scales
CONFIG["palette"]["D"] = (184, 182, 176, 255)  # darker armor
CONFIG["palette"]["C"] = (236, 178, 88, 255)   # amber membrane
CONFIG["palette"]["S"] = (216, 150, 70, 255)   # warm scale dashes
