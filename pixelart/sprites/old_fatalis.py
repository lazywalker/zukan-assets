"""Old Fatalis, fatalis variant. The legendary white: white-fatalis aged
with a deeper blue-white chest and a paler horn sheen."""
from white_fatalis import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "old-fatalis"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (238, 236, 232, 255)  # aged pearl scales
CONFIG["palette"]["D"] = (200, 198, 194, 255)  # darker aged white
CONFIG["palette"]["C"] = (140, 188, 232, 255)  # deep ice-blue chest
