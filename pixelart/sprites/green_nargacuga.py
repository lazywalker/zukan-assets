"""Green Nargacuga, nargacuga subspecies. Moss-green fur over the stealth
panther frame, blade edge kept silver."""
from nargacuga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "green-nargacuga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (62, 86, 60, 255)     # moss-green fur
CONFIG["palette"]["D"] = (44, 62, 44, 255)     # darker green
CONFIG["palette"]["B"] = (78, 104, 74, 255)    # green wing-blades
