from Piecers import *
from numpy import ndenumerate
import pygame

class Shift:

    def __init__(self):
        self.screenPos = (500, 200)
        self.shapeID = -1
        self.shape = None
    
    def getShapeID(self):
        return self.shapeID
    
    def getShape(self):
        return self.shape
    
    def swapFirst(self, currentP: Piece):
        self.shapeID = currentP.getShapeID()
        self.shape = currentP.getShape()
        
    def swap(self, currentP: Piece):
        self.shapeID = currentP.getShapeID()
        self.shape = currentP.getShape()
        currentP.setShapeID(self.shapeID)
        currentP.setShape(self.shape)
    
    def showShift(self, screen, colorList, size):

        def paintCell(screen, color: list, pos: tuple):
            """paints a cell"""
            posX = pos[1] * size + self.screenPos[1]
            posY = pos[0] * size + self.screenPos[1]
            pygame.draw.rect(screen, color, (posX, posY, size, size))
        
        for pos, cell in ndenumerate(self.shape):
            paintCell(screen, colorList[cell], pos)