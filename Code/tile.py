import pygame, sys 
from pytmx.util_pygame import load_pygame
from settings import * 
class TiledMap(pygame.sprite.Sprite):
    def __init__(self, pos , surf , groups) : 
        super().__init__() 
        self.image = surf 
        self.rect = self.image.get_rect(topleft = pos)

pygame.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
tmx_data = load_pygame('./Assets/tmx/untitled.tmx') 

sprite_group = pygame.sprite.Group() 

for layer in tmx_data.layers: 
    if hasattr(layer, 'data'): 
            for x , y , surf in layer.tiles(): 
                pos = (x *128, y * 128)
                TiledMap(pos = pos, surf = surf, groups = sprite_group) 

    def draw (self, sprite_group): 
         sprite_group.draw(screen) 
          

     