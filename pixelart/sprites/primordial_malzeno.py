"""Primordial Malzeno, malzeno variant. The untainted knight: pristine
white-silver over the crimson knight frame with pale blue blood-wings."""
from malzeno import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "primordial-malzeno"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["S"] = (232, 232, 236, 255)  # pristine white scales
CONFIG["palette"]["D"] = (192, 192, 198, 255)  # darker silver
CONFIG["palette"]["R"] = (150, 158, 190, 255)  # pale blue wings
CONFIG["palette"]["r"] = (114, 122, 158, 255)  # darker blue edges
