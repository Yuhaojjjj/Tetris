from Griders import *
from Piecers import *
from Utils import *
import json

pieces, colors = getSettings().values()

grid = Static(10, 20)
piece = Piece(0, pieces)

print(piece.canGoTo(grid, "r"))