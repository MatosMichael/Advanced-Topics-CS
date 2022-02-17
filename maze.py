from operator import truediv
from random import randrange
import random
import pygame
import sys
pygame.init()

width = 500
height = 500
room_size = 50
adjacent = []
grid = [[{
    "visited": False,
    "north": True,
    "south": True,
    "east": True,
    "west": True
} for i in range(width//room_size)] for j in range(height//room_size)]


def add_adjacent(x, y):
    if (x >= 0) and (y >= 0) and (y < len(grid)) and (x < len(grid[y])) and (grid[y][x].get("visited") == False):
        adjacent.append([x, y])


def mark(x, y):
    grid[y][x]["visited"] = True
    add_adjacent(x-1, y)
    add_adjacent(x+1, y)
    add_adjacent(x, y-1)
    add_adjacent(x, y+1)


screen = pygame.display.set_mode((width, height))
x, y = random.randrange(width//room_size), random.randrange(height//room_size)
mark(x, y)
while True:
    if len(adjacent):
        next = random.randrange(len(adjacent))
        [nx, ny] = adjacent[next]
        del adjacent[next]
        mark(nx, ny)
        try:
            if ny > y:
                grid[y][x]["north"] = False
            elif ny < y:
                grid[y][x]["south"] = False
            elif nx > x:
                grid[y][x]["east"] = False
            else:
                grid[y][x]["west"] = False
        except IndexError:
            print(x)
            print(y)
        x, y = nx, ny
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]["visited"] == True:
                left = i * room_size
                top = j * room_size
                north, south, east, west, last = 0, 0, 0, 0, 0
                if i == len(grid[i]) - 1:
                    last = 1
                if grid[i][j]["north"] == True:
                    north = 1
                    # pygame.draw.line(screen, (0,0,0), (left, top), (left + room_size, top))
                if grid[i][j]["south"] == True:
                    south = 1
                    # pygame.draw.line(screen, (0,0,0), (left, top + room_size), (left + room_size, top + room_size))
                if grid[i][j]["east"] == True:
                    east = 1
                    # pygame.draw.line(screen, (0,0,0), (left + room_size, top), (left + room_size, top + room_size))
                if grid[i][j]["west"] == True:
                    west = 1
                    # pygame.draw.line(screen, (0,0,0), (left, top), (left, top + room_size))
                pygame.draw.rect(
                    screen, (255, 255, 255), (left + west, top + north, room_size - last - east, room_size - south))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    pygame.time.Clock().tick(60)
