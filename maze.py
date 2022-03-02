from operator import truediv
from random import randrange
import random
import pygame
import sys
import pdb
pygame.init()

width = 500
height = 500
room_size = 50
num_rooms = (width*height // room_size**2)
num_columns = width // room_size
num_rows = height // room_size
def generate_walls(index):
    ret = []

    cell_x = index
    cell_col = 0
    while cell_x >= num_columns:
        cell_x -= num_columns
        cell_col += 1

    cell_y = index
    cell_row = 0
    while cell_y >= num_rows:
        cell_y -= num_rows
        cell_row += 1

    cell_x *= room_size
    cell_y = cell_row * room_size

    # top wall
    ret.append({
        "cells": [index, index - num_columns],
        "points": [(cell_x, cell_y), (cell_x + room_size, cell_y)]
    })
    #   bottom wall
    ret.append({
        "cells": [index, index + num_columns],
        "points": [(cell_x, cell_y + room_size), (cell_x + room_size, cell_y + room_size)]
    })
    # left wall
    ret.append({
        "cells": [index - 1, index],
        "points": [(cell_x , cell_y), (cell_x, cell_y + room_size)]
    })
    # right wall
    ret.append({
        "cells": [index + 1, index],
        "points": [(cell_x + room_size, cell_y), (cell_x + room_size, cell_y + room_size)]
    })
    
    return ret

_walls = [generate_walls(i) for i in range(num_rooms)]
walls = [wall for sublist in _walls for wall in sublist]

adjacent = [0]

def add_adjacent(i):
    for wall in walls:
        if (wall["cells"].count(i) > 0):
            if wall["cells"].index(i) == 0:
                prox = (wall["cells"][1])
            else:
                prox = (wall["cells"][0])
            if prox > 0 and adjacent.count(prox) == 0:
                adjacent.append(prox)
current = 0
screen = pygame.display.set_mode((width, height))
while True:
    screen.fill("black")
    add_adjacent(current)
    if len(adjacent):
        adjacent.remove(current)
        prox = adjacent[random.randrange(len(adjacent))]
        walls = [wall for wall in walls if wall["cells"].count(prox) == 0 or wall["cells"].count(current) == 0]
        current = prox
    for wall in walls:
        pygame.draw.line(screen, (255,255,255), wall["points"][0], wall["points"][1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    pygame.time.Clock().tick(60)
