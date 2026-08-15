"""White Fatalis, fatalis variant. The ancient white dragon: pearl-white
scales over the black dragon frame with an ice-blue chest glow."""
from fatalis import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "white-fatalis"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (226, 224, 218, 255)  # pearl-white scales
CONFIG["palette"]["D"] = (184, 182, 178, 255)  # darker white
CONFIG["palette"]["C"] = (168, 204, 232, 255)  # ice-blue chest glow
