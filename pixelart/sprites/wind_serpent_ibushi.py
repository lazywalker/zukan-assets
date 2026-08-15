"""Wind Serpent Ibushi, elder dragon. The male storm: ibushi's serpentine
frame in pale grey-green with a great curling horn pair and gold ring
crest, winding right like narwa but leaner."""
from narwa_the_allmother import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "wind-serpent-ibushi"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (188, 196, 186, 255)  # pale grey-green body
CONFIG["palette"]["D"] = (150, 158, 148, 255)  # body shade
CONFIG["palette"]["Y"] = (216, 188, 92, 255)   # gold ring crest
CONFIG["palette"]["N"] = (64, 66, 60, 255)     # dark horn edges
CONFIG["palette"]["C"] = (216, 222, 212, 255)  # bright underside
