"""Ice Chramine, chramine variant. The frost rooster: ice-white plumage
over the cloud rooster frame with a frozen pouch."""
from chramine import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "ice-chramine"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (218, 228, 238, 255)  # ice-white plumage
CONFIG["palette"]["D"] = (160, 180, 200, 255)  # darker ice
CONFIG["palette"]["F"] = (192, 212, 230, 255)  # frozen pouch

# the frost rooster: crest feathers stiffen into icy spikes
CONFIG["spans"] = {
    **_base["spans"],
    2:  [(4, 4), (6, 6)],
    3:  [(3, 7)],
}
