"""Planar screening only; no mechanical approval. Python 3 stdlib."""
import math

def screen(board_width, inner_bolt=12):
    stack_r = 25.5 / math.sqrt(2)
    hole_r = 1.1
    root_start, root_end, root_half = 8, 30, 5
    outer_bolt = 26
    return {
        "adjacent_root_gap": math.sqrt(2)*(root_start-root_half),
        "guide_side_clearance": (10.3-10)/2,
        "inner_end_ligament": inner_bolt-root_start-hole_r,
        "outer_end_ligament": root_end-outer_bolt-hole_r,
        "inner_stack_gap": abs(stack_r-inner_bolt)-5.5,
        "outer_stack_gap": abs(outer_bolt-stack_r)-5.5,
        "outer_board_diagonal_gap": outer_bolt-board_width/math.sqrt(2),
        "stack_intersects_root": root_start < stack_r < root_end,
    }

if __name__ == "__main__":
    for name, width in (("mini3",31.3),("mini35",33)):
        print(name, screen(width))
    print("REVIEW REQUIRED: stack interface, guides, tool access, load tests.")
