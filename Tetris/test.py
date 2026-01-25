import func.grid as grid
import func.piece as piece
import json
import os
import numpy as np
import time
with open(r"C:\Users\jiayu\OneDrive\Python\Tetris\config.json") as f:
    config = json.load(f)

current_arr = np.array(config["pieces"]["4"])

t_current_arr = current_arr.T[::-1]

print(current_arr)
print(t_current_arr)

t_current_arr = t_current_arr.T[::-1]
print(t_current_arr)

#logic for rotating pieces. idk how to make srs