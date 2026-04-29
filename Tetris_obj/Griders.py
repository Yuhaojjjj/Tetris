from __future__ import annotations

from numpy import ndenumerate, zeros, delete, vstack
import pygame
from Piecers import *
from Shifter import *
from Utils import getColor

class Grid:

    # Constructor
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.content = zeros([h, w], dtype = int)
    
    # Attributes
    def getContent(self):
        return self.content
    
    def getW(self):
        return self.w
    
    def getH(self):
        return self.h

class Final(Grid):

    # Constructor
    def __init__(self, w, h):
        super().__init__(w, h)
    
    # Methods
    def paintGrid(self, screen, colorList, size, shift: Shift) -> None:
        """paint the grid within the current shift"""

        def paintCell(screen, color: list, size: int, pos: tuple) -> None:
            """paints a cell"""
            pygame.draw.rect(screen, color, (pos[1] * size, pos[0] * size, size, size))
        
        if shift.getShapeID() != -1:
            
            shape = shift.getShape()
            for pos, cell in ndenumerate(shape):
                
                if cell != 0:
                    paintCell(screen, getColor(cell, colorList), size, pos)

        for pos, cell in ndenumerate(self.content):

            if cell != 0:
                paintCell(screen, getColor(cell, colorList), size, pos)

            else:
                pygame.draw.rect(screen, (20, 20, 20), (pos[1] * size, pos[0] * size, size, size), width = 1)

    def update(self, Grid1: Grid, Grid2: Grid):
        self.content = Grid1.getContent() + Grid2.getContent()

class Static(Grid):

    # Constructor
    def __init__(self, w, h):
        super().__init__(w, h)

    # Attributes
    def setPiece(self, currentP: Piece):

        for (y, x), cell in ndenumerate(currentP.getShape()):
            if cell != 0:
                self.content[y + currentP.getY()][x + currentP.getX()] = cell

    def clearLines(self):

        rowsToClear = []
        zerosRow = zeros([1, self.w], dtype = int)

        for y, row in enumerate(self.content):
            if 0 not in row:
                rowsToClear.append(y)
        
        if len(rowsToClear):
            self.content = delete(self.content, rowsToClear, axis = 0)

            for i in rowsToClear:
                self.content = vstack([zerosRow, self.content])

class Moving(Grid):

    # Constructor
    def __init__(self, w, h):
        super().__init__(w, h)
    
    # Attributes
    def clear(self, currentP):
        for (y, x), cell in ndenumerate(currentP.getShape()):
            if cell != 0:
                self.content[y + currentP.getY()][x + currentP.getX()] = 0
    
    def update(self, currentP):
        for (y, x), cell in ndenumerate(currentP.getShape()):
            if cell != 0:
                self.content[y + currentP.getY()][x + currentP.getX()] = cell