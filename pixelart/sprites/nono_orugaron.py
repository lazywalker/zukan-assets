"""Nono Orugaron, fanged beast. The dawn wolf: lunagaron's wolf frame in
pale moonlight fur with a sweeping tail plume."""
from lunagaron import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "nono-orugaron"
CONFIG["compare_to"] = ""
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["F"] = (226, 224, 232, 255)  # moonlight fur
CONFIG["palette"]["D"] = (188, 186, 196, 255)  # lighter shade
CONFIG["palette"]["M"] = (140, 138, 152, 255)  # pale mane
CONFIG["palette"]["V"] = (188, 132, 138, 255)  # rose claws

# sweeping tail plume longer
CONFIG["spans"] = {
    **_base["spans"],
    18: [(9, 14), (18, 22)],
    19: [(9, 12), (19, 23)],
    20: [(10, 11), (20, 23)],
    21: [(10, 10), (21, 22)],
}
