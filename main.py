
#---------IMPORTS---------# 
import pygame, sys , os
from settings import * 
#---------IMPORTS---------#

#---------INITIALISATION---------#
pygame.init() 
screen = pygame.display.set_mode((SCREEN_HEIGHT ,  SCREEN_WIDTH))
clock = pygame.time.Clock() 
#---------INITIALISATION---------#

#---------Main Game Loop----------#
run = True
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()
    screen.fill("BLACK") 
    pygame.display.update() 
    clock.tick(60)  # Forces a game update to happen 60 times a second. This could cause the game to break if set to a higher refresh rate as more updates are being done.

