"""Sand Barioth, barioth subspecies. Desert-tan hide over the sabertooth
frame, the stripes turned darker sand."""
from barioth import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "sand-barioth"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["W"] = (214, 188, 140, 255)  # desert-tan coat
CONFIG["palette"]["S"] = (164, 138, 96, 255)   # darker sand stripes
CONFIG["palette"]["D"] = (126, 104, 70, 255)   # darker shade
CONFIG["palette"]["L"] = (228, 208, 168, 255)  # pale belly
