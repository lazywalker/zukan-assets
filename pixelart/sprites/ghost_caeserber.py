"""Ghost Caeserber, amphibian. The bog ghost: tetsucabra's toad frame in a
sickly green glow with hollow pale eyes."""
from tetsucabra import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ghost-caeserber"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (128, 148, 110, 255)  # sickly green hide
CONFIG["palette"]["D"] = (96, 114, 82, 255)    # darker green
CONFIG["palette"]["C"] = (208, 214, 178, 255)  # pale jaw
CONFIG["palette"]["W"] = (240, 244, 230, 255)  # hollow eyes
