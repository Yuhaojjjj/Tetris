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

    # Getters and setters
    def getShape(self) -> list[list]:
        return self.shape
    
    def getShapeID(self) -> int:
        return self.shapeID
    
    def getX(self) -> int:
        return self.X

    def getY(self) -> int:
        return self.Y

    def setShapeID(self, shapeID):
        self.shapeID = shapeID
    
    def setShape(self, shape):
        self.shape = shape
    # Methods
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

        newK = (self.K + K) % 4

        def getOffsets():
            if self.shapeID < 5:
                return (array(offsets["not i"][newK]) - array(offsets["not i"][self.K]))
            else:
                return (array(offsets["i"][newK]) - array(offsets["i"][self.K]))
        
        offsets = getOffsets()

        i = 0
        for offset in offsets:
            i += 1
            if self.canFitIn(G, K, offset):
                print(i)
                return(self.X + offset[0], self.Y + offset[1])
        print(i)
        return None

    def canFitIn(self, G, K = 0, offset = None) -> bool:

        """
        this function checks if the cells where the pieces wants to fit in are available
        """

        newX = self.X + offset[0]
        newY = self.Y + offset[1]
        newShape = rot90(self.shape, k = K)
        content = G.getContent()

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
                    return False
        return True
                

    def hardDrop(self, G):
        while self.canFitIn(G, offset = [0, 1]):
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

            coords = self.getRotationCoords(staticG, K, offsets)
            print(coords)
            if coords != None:
                self.X, self.Y = coords
                self.shape = rot90(self.shape, K)
                self.K = newK
            
            else:
                print("did not rotate")