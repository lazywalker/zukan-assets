"""Shrouded Nerscylla, nerscylla subspecies. The corpse-cloaked spider:
deep purple hood and dusk-grey body over the nerscylla frame, the
abdomen mark turned red."""
from nerscylla import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "shrouded-nerscylla"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["C"] = (122, 108, 134, 255)  # dusk-grey body
CONFIG["palette"]["D"] = (92, 80, 104, 255)    # darker shade
CONFIG["palette"]["V"] = (66, 46, 92, 255)     # deep purple hood
CONFIG["palette"]["W"] = (232, 108, 96, 255)   # red abdomen mark
