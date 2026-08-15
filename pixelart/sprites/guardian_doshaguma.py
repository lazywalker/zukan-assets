"""Guardian Doshaguma, doshaguma variant. The constructed guardian: milky
white fur over the shaggy bear frame with an amber eye glow."""
from doshaguma import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "guardian-doshaguma"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (220, 218, 210, 255)  # milky white fur
CONFIG["palette"]["D"] = (184, 182, 174, 255)  # darker fur
CONFIG["palette"]["R"] = (172, 168, 158, 255)  # pale grey face
CONFIG["palette"]["N"] = (236, 178, 88, 255)   # amber eye glow
