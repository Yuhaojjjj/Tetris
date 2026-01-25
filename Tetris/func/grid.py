import numpy as np

def new(w, h):
    grid = []
    for y in range(h):
        grid.append([0 for x in range(w)])
    return grid

def join(static_g, falling_g):
    return (np.array(static_g) + np.array(falling_g))