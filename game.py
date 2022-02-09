from logging import raiseExceptions
import pygame
import sys
import random

pygame.init()

width = 600
height = 800


RED = (255, 0, 0)
GREEN = (0, 255, 0)
player_size = 20
goal_size = 50
player = pygame.Rect(275, height - player_size, player_size, player_size)
goal = pygame.Rect(random.randrange(width - goal_size), 0, goal_size, goal_size)
screen = pygame.display.set_mode((width, height))
h_walls = [(0, 0, width, 0), (0, height, width, height)]
v_walls = [(0, 0, 0, height), (width, 0, width, height)]

game_over = False

while True:
    if game_over:
        #PLACE Text HERE
        raise Exception("You Won!")
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player.left not in [i[0] for i in v_walls]:
                player = player.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            if player.right not in [i[0] for i in v_walls]:
                player = player.move(1, 0)
        if keys[pygame.K_UP]:
            if player.top not in [i[1] for i in h_walls]:
                player = player.move(0, -1)
        if keys[pygame.K_DOWN]:
            if player.bottom not in [i[1] for i in h_walls]:
                player = player.move(0, 1)

        

        if player.colliderect(goal):
            game_over = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, GREEN, goal)
        pygame.draw.rect(screen, RED, player)
    pygame.time.Clock().tick(800)
    pygame.display.update()