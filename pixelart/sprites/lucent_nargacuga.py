"""Lucent Nargacuga, nargacuga subspecies. The pale phantom: moonlight
white fur over the stealth panther frame, blade edge turned deep teal."""
from nargacuga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "lucent-nargacuga"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (206, 208, 216, 255)  # moonlight fur
CONFIG["palette"]["D"] = (166, 168, 178, 255)  # darker fur
CONFIG["palette"]["B"] = (178, 180, 190, 255)  # pale wing-blades
CONFIG["palette"]["S"] = (58, 128, 128, 255)   # teal blade edge
