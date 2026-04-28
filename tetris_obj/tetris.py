from Griders import *
from Piecers import *
from Bagger import *
import Utils
import pygame

"""settings"""
cooldown = 500 # ms
size = 32 # px

"""debug"""
gravity = True

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

def main():

    # values inicialization
    lastFall = 0
    
    # Set grids
    staticG = Static(10, 20)
    movingG = Moving(10, 20)
    finalG = Final(10, 20)
    
    # Get settings done
    pieces, colors, srs = Utils.getSettings().values()

    # Get bag done
    currentBag = Bag()

    # Place first piece
    currentP = Piece(currentBag.pop(), pieces)

    running = True
    while running:

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Controls
                if event.key == pygame.K_a:
                    print("got pressed")
                    if currentP.canFitIn(staticG, offsets = [-1, 0]):
                        movingG.clear(currentP)
                        currentP.goLeft()
                        movingG.update(currentP)

                if event.key == pygame.K_d:
                    if currentP.canFitIn(staticG, offsets = [1, 0]):
                        movingG.clear(currentP)
                        currentP.goRight()
                        movingG.update(currentP)
                
                if event.key == pygame.K_w:
                    if currentP.canFitIn(staticG, offsets = [0, 1]):
                        movingG.clear(currentP)
                        currentP.goDown()
                        movingG.update(currentP)

                if event.key == pygame.K_s:
                        movingG.clear(currentP)
                        currentP.hardDrop(staticG)
                        movingG.update(currentP)
                
                if event.key == pygame.K_LEFT:
                    movingG.clear(currentP)
                    currentP.rotate(staticG, 3, srs)
                    movingG.update(currentP)

                if event.key == pygame.K_RIGHT:
                    movingG.clear(currentP)
                    currentP.rotate(staticG, 1, srs)
                    movingG.update(currentP)

                if event.key == pygame.K_UP:
                    movingG.clear(currentP)
                    currentP.rotate(staticG, 2, srs)
                    movingG.update(currentP)

        # Falling Mechanic
        if gravity == True and lastFall >= cooldown:
            lastFall = 0

            if currentP.canGoTo(staticG, "d"):
                movingG.clear(currentP)
                currentP.goDown()
                movingG.update(currentP)

            else:
                # Line clearing mechanic
                staticG.setPiece(currentP)
                staticG.clearLines()

                movingG.clear(currentP)
                currentP = Piece(currentBag.pop(), pieces)
                movingG.update(currentP)
        
        # Updating and showing
        finalG.update(movingG, staticG)
        finalG.paintGrid(screen, colors, size)

        pygame.display.flip()

        # Getting ms
        delta = clock.tick(60)
        lastFall += delta

    pygame.quit()

main()