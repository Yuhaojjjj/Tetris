from __future__ import annotations

from Griders import *
from numpy import ndenumerate, rot90, array
class Piece:

    # Constructor
    def __init__(self, shapeID, shapeList):
        self.shapeID = shapeID
        self.shape = shapeList[self.shapeID]
        self.X = 3
        self.Y = 0
        self.K = 0

    # Attributes
    def getShape(self) -> list[list]:
        return self.shape
    
    def getX(self) -> int:
        return self.X

    def getY(self) -> int:
        return self.Y
    
    def canRotate(self, G, K) -> bool:

        rotated = rot90(self.shape, k = K)
        content = G.getContent()

        for(y, x), cell in ndenumerate(rotated):
            if cell != 0:

                condition1 = self.Y + y > G.getH() - 1 or self.X + x < 0 or self.X + x > G.getW() - 1
                if condition1 or content[self.Y + y][self.X + x] != 0:
                    return False
        return True
    
    def getRotationCoords(self, G, K, offsets):
        """
        this function returns the x and y coordinates after rotating the piece,
        according to the tetris SRS standarts
        """
        def getOffsets():
            if self.shapeID < 5:
                return (offsets["not i"][K] - offsets["not i"][self.K])
            else:
                return (offsets["i"][K] - offsets["i"][self.K])
        
        


    def canFitIn(self, G, K = 0, offset = None) -> bool:

        newX = self.X
        newY = self.Y
        newShape = self.shape
        content = G.getContent()

        if offset:
            newX += offset[0]
            newY += offset[1]
        
        if K:
            newShape = rot90(newShape, k = K)
        
        def getsOutOfGrid(cellY, cellX):

            if cellY >= 20:
                return True
            if cellX >= 10:
                return True
            if cellX <= -1:
                return True
            
            return False
        
        for (y, x), cell in ndenumerate(newShape):

            if cell != 0:

                cellY = newY + y
                cellX = newX + x

                if getsOutOfGrid(cellY, cellX) or content[cellY][cellX] != 0:
                    print("dont go", cellY, cellX)
                    return False
        
        print("go")
        return True
                

    def hardDrop(self, G):
        while self.canGoTo(G, "d"):
            self.goDown()
    
    def goRight(self):
        self.X += 1
    
    def goLeft(self):
        self.X -= 1
    
    def goDown(self):
        self.Y += 1
    
    def rotate(self, staticG, K, offsets):

        newK = (self.K + K) % 4
        
        if self.shapeID != 6:
            self.Y, self.X = self.getRotationCoords(staticG, newK, offsets)