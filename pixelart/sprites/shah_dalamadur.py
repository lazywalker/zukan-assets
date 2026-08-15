"""Shah Dalamadur, dalamadur variant. The king coiled: warmer golden-grey
scales over the world serpent frame with a red-eyed crown."""
from dalamadur import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shah-dalamadur"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (176, 158, 120, 255)  # golden-grey scales
CONFIG["palette"]["D"] = (140, 124, 92, 255)   # darker gold
CONFIG["palette"]["C"] = (214, 198, 160, 255)  # pale underside
