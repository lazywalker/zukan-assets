"""Rhenoplos, herbivore subspecies. The stubborn rammer: khaki plate over
the apceros frame with a taller dome and blunt pale spikes."""
from apceros import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rhenoplos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["B"] = (128, 124, 108, 255)  # khaki plate
CONFIG["palette"]["D"] = (98, 94, 80, 255)     # darker plate
CONFIG["palette"]["C"] = (196, 192, 172, 255)  # blunt pale spikes

# dome raised one row with blunt spikes
CONFIG["spans"] = {
    **_base["spans"],
    1:  [(8, 8), (14, 15), (21, 21)],
}
