"""Silver Hypnocatrice, hypnocatrice variant (Frontier). Silver-white
plumage with the crest slicked flat back, a sleek low profile against
the base bird's upright crest. No game icon exists, so compare_to is
empty."""
from hypnocatrice import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "silver-hypnocatrice"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["G"] = (205, 205, 215, 255)  # silver plumage
CONFIG["palette"]["Y"] = (238, 238, 242, 255)  # pale face and belly
CONFIG["palette"]["F"] = (160, 160, 178, 255)  # crest / shade
CONFIG["palette"]["S"] = (130, 130, 150, 255)  # spots

# sleek swept-back crest: upright fan removed, low saddle only
CONFIG["spans"] = {
    **_base["spans"],
    3:  [],
    4:  [(6, 12)],
    5:  [(5, 12)],
}
