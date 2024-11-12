from pytmx import load_pygame
import pygame 
from settings import * 
#Class Tile manages the map 
class Tile(pygame.sprite.Sprite): 
    def __init__(self,pos,surf,groups): 
        super().__init__(groups) 
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos) 

pygame.init() 
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
tmx_data = load_pygame('./Assets/tmx/untitled.tmx')
sprite_group = pygame.sprite.Group() 

for layer in tmx_data.visible_layers: 
    if hasattr(layer,'data'): 
        for x,y,surf in layer.tiles(): 
            pos = (x * 128, y * 128) 
            Tile(pos = pos , surf = surf, groups = sprite_group)

for obj in tmx_data.objects: 
    pos = obj.x,obj.y
    if obj.image: 
        Tile(pos = pos , surf = surf , groups = sprite_group) 
        