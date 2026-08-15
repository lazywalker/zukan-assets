"""Scarred Yian Garuga, garuga variant. The worn old warrior: crest
drooped low on the head, silver spikes kept, pale old scars across the
flank and neck. Derive of yian-garuga with a lowered crest."""
from yian_garuga import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "scarred-yian-garuga"
CONFIG["compare_to"] = ""

# drooping crest: saddle sits one row lower, tip row gone
CONFIG["spans"] = {
    **_base["spans"],
    2:  [],
    3:  [(5, 12)],
    4:  [(4, 13)],
}
CONFIG["fills"] = list(_base["fills"]) + [
    # pale scars across the flank and neck
    ("runs", [(10, 22, 23), (11, 24, 25)], "C"),
    ("runs", [(12, 17, 17), (13, 18, 18), (14, 19, 19)], "C"),
]
