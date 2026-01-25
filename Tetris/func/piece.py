import random

def getw(piece):
    return (len(piece[0]))

def geth(piece):
    return (len(piece))

def new(piece, startpos, falling_g):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            falling_g[y][startpos + x] = piece[y][x]

def canfall(piece, pos, static_g):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                if (pos[0] + y + 1) >= len(static_g) or static_g[y + pos[0] + 1][x + pos[1]] != 0 :
                    return False
    return True

def fall(piece, pos, falling_g):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                falling_g[y + pos[0]][x + pos[1]] = 0

    pos[0] = pos[0] + 1
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                falling_g[y + pos[0]][x + pos[1]] = cell

def set(piece, pos, static_g, falling_g):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell != 0:
                static_g[y + pos[0]][x + pos[1]] = cell
                falling_g[y + pos[0]][x + pos[1]] = 0
    
def select(piecelist):
    piece = piecelist.pop(0)
    return piece

def listnew(piecelist):
    piecelist = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(piecelist)
    return piecelist