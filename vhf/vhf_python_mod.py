# this module will be imported in the into your flowgraph
import sys
from typing import Final

F1: Final[int] = 161_000_000
F2: Final[int] = 163_000_000
STEP: Final[int] = 25_000
f = F1

def sweeper(prob_lvl1):
    global f

    if prob_lvl1 == 0.0:
        f += STEP
    if f >= F2:
        f = F1

    print(prob_lvl1, f)
    return f
