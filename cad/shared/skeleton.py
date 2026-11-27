"""Concept geometry only; no manufacturing output. Python 3 stdlib."""
import csv
import math
from pathlib import Path

def load(variant):
    if variant not in ("mini3", "mini35"):
        raise ValueError(variant)
    with Path(__file__).with_name("parameters.csv").open() as f:
        return {row["name"]: float(row[variant]) for row in csv.DictReader(f)}

def geometry(p):
    w = p["wheelbase"]
    a = w / (2 * math.sqrt(2))
    s = p["stack_pitch"] / 2
    motors = [(x*a, y*a) for x in (-1,1) for y in (-1,1)]
    stack = [(x*s, y*s) for x in (-1,1) for y in (-1,1)]
    # Candidate two-bolt layout on each diagonal, NOT approved.
    screws = [(x*d/math.sqrt(2), y*d/math.sqrt(2))
              for x in (-1,1) for y in (-1,1)
              for d in (p["retainer_radius"], p["retainer_outer_radius"])]
    gap = w/math.sqrt(2)-p["prop_diameter"]
    clearance = min(math.dist(h, k) for h in screws for k in stack)
    clearance -= p["retainer_head_radius"] + p["stack_keepout_radius"]
    return dict(motors=motors, stack=stack, screws=screws,
                prop_gap=gap, retainer_stack_clearance=clearance)

if __name__ == "__main__":
    for variant in ("mini3", "mini35"):
        g = geometry(load(variant))
        print(variant, g)
        print("Nominal checks:", "prop gap OK" if g["prop_gap"] >= 4 else "prop gap FAIL",
              "retainer plan gap OK" if g["retainer_stack_clearance"] >= 0 else "retainer plan gap FAIL")
        print("NOT a mechanical, vertical clearance or manufacturing approval.")
