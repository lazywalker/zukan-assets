"""Great Dracophage Bug, neopteron. The dragon bolt: great-thunderbug's
swollen frame in deep violet with hot pink lightning bands."""
from great_thunderbug import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-dracophage-bug"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (96, 66, 146, 255)    # violet body
CONFIG["palette"]["Y"] = (240, 118, 158, 255)  # pink lightning bands
CONFIG["palette"]["D"] = (68, 46, 108, 255)    # darker violet
CONFIG["palette"]["W"] = (244, 226, 250, 255)  # bright wings
