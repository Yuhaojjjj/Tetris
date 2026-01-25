import numpy as np

def move(piece, pos, falling_g, direction):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                falling_g[y + pos[0]][x + pos[1]] = 0
    
    if direction == "right":
        pos[1] += 1
    elif direction == "left":
        pos[1] -= 1
    
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                falling_g[y + pos[0]][x + pos[1]] = 0

def canmove(piece, pos, static_g, direction):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                if direction == "right":
                    if (pos[1] + x + 1) >= len(static_g[0]) or static_g[y + pos[0]][x + pos[1] + 1] != 0 :
                        return False
                elif direction == "left":
                    if (pos[1] + x - 1) < 0 or static_g[y + pos[0]][x + pos[1] - 1] != 0 :
                        return False
    return True

def turn(piece, pos, falling_g, rotation):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                falling_g[y + pos[0]][x + pos[1]] = 0

    rotated_piece = np.array(piece)
    if rotation == 90:
        rotated_piece = rotated_piece.T[:, ::-1]
    elif rotation == 270:
        rotated_piece = rotated_piece.T[::-1]
    elif rotation == 180:
        rotated_piece = rotated_piece[::-1, ::-1]
    
    return rotated_piece.tolist()