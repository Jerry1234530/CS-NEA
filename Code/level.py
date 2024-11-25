import pygame
from settings import * 
from player import Player 
from pytmx import load_pygame
import pytmx
class Level: 
    def __init__(self): 
        self.display_surface = pygame.display.get_surface()  
        self.all_sprites = pygame.sprite.Group() 
        self.tmx_data = load_pygame('./Assets/tmx/untitled.tmx')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



    def setup(self): 
        self.player = Player((640,360) , self.all_sprites)

    def run(self, dt): 
        self.display_surface.fill(BLACK) 
        self.all_sprites.draw(self.display_surface)

print('DEBUG: The Pygame Window is currently running')

 