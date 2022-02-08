import pygame
import sys
 
pygame.init()
 
width = 600
height = 800
 
 
RED = (255, 0, 0)
player_pos = [275, 700]
player_size = 50
 
screen = pygame.display.set_mode((width, height))
 
game_over = False
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5
            elif event.key == pygame.K_UP:
                y -= 5
            elif event.key == pygame.K_DOWN:
                y += 5
            player_pos = [x,y]
 
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
 
    pygame.display.update()
 

