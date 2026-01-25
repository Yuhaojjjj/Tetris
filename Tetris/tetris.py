import pygame as pg
import numpy as np
import random
import func.grid as grid
import func.piece as piece
import func.control as control
import json
pg.init()

w, h = 800, 600

size = 24
bag_size = 7

falling_time = 500
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
running = True

with open(r"C:\Users\jiayu\OneDrive\Python\Tetris\config.json") as f:
    config = json.load(f)

piecelist = []
piecelist = piece.listnew(piecelist)

print(config.keys())

print(piecelist)

current_piece = config["pieces"][str(piece.select(piecelist))]

pos = [0, config["startpos"]]
static_g = grid.new(config["gw"], config["gh"])
falling_g = grid.new(config["gw"], config["gh"])

piece.new(current_piece, pos[1], falling_g)

def drawblock(y, x, btype):
    rectv = (x * size, y * size, size, size)
    color = config["colors"][str(btype)]
    pg.draw.rect(screen, color, rectv)
    pg.draw.rect(screen, (50, 50, 50), rectv, 1)

def drawgrid(g):
    for y, row in enumerate(g):
        for x, cell in enumerate(row):
            drawblock(y, x, cell)
    
last_fall = 0

while running:
    last_fall += clock.tick(60)
    
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                if control.canmove(current_piece, pos, static_g, "left"):
                    control.move(current_piece, pos, falling_g, "left")
            if event.key == pg.K_d:
                if control.canmove(current_piece, pos, static_g, "right"):
                    control.move(current_piece, pos, falling_g, "right")
            if event.key == pg.K_LEFT:
                current_piece = control.turn(current_piece, pos, falling_g, 90)
            if event.key == pg.K_RIGHT:
                current_piece = control.turn(current_piece, pos, falling_g, 270)
            if event.key == pg.K_UP:
                current_piece = control.turn(current_piece, pos, falling_g, 180)

    total_g = grid.join(static_g, falling_g)
    if last_fall >= falling_time:
        last_fall = 0
        if piece.canfall(current_piece, pos, static_g):
            piece.fall(current_piece, pos, falling_g)
        else:
            piece.set(current_piece, pos, static_g, falling_g)
            if len(piecelist) == 0:
                piecelist = piece.listnew(piecelist)
            current_piece = config["pieces"][str(piece.select(piecelist))]
            pos = [0, config["startpos"]]


    drawgrid(total_g)
    pg.display.flip()

pg.quit()