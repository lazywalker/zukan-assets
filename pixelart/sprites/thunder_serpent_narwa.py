"""Thunder Serpent Narwa, elder dragon. The storm coil: narwa's serpent
frame in storm blue-white with electric yellow rings and a charged crown."""
from narwa_the_allmother import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "thunder-serpent-narwa"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (198, 208, 226, 255)  # storm blue-white body
CONFIG["palette"]["D"] = (158, 168, 188, 255)  # darker storm
CONFIG["palette"]["Y"] = (126, 188, 240, 255)  # electric blue rings
CONFIG["palette"]["N"] = (52, 62, 84, 255)     # dark horn edges
CONFIG["palette"]["C"] = (222, 230, 242, 255)  # bright underside
