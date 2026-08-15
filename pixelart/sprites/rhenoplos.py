"""Rhenoplos, herbivore subspecies. The stubborn rammer: bluish-grey
plate over the apceros frame, a taller round dome with blunt spikes, and
the tail club reduced to a blunt wedge."""
from apceros import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "rhenoplos"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["R"] = (128, 124, 108, 255)  # khaki plate
CONFIG["palette"]["D"] = (98, 94, 80, 255)     # darker plate
CONFIG["palette"]["S"] = (196, 192, 172, 255)  # blunt pale spikes

# taller dome + blunt tail
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(9, 9), (16, 16)],
    15: [(5, 24), (19, 27)],
    16: [(6, 23), (20, 26)],
}
