import pygame, sys , os
from settings import * 


os.environ["SDL_AUDIODRIVER"] = "dsp"
pygame.init() 
screen = pygame.display.set_mode((SCREEN_HEIGHT ,  SCREEN_WIDTH))
clock = pygame.time.Clock() 
run = True
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()
    screen.fill("BLACK") 
    pygame.display.update() 
    clock.tick(60)  

