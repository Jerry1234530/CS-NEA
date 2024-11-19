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

    def draw_map(self):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):  # Only process tile layers
                for x, y, gid in layer:  # Iterate through tiles
                    if gid != 0:  # Skip empty tiles (gid == 0)
                        tile = self.tmx_data.get_tile_image_by_gid(gid)
                        if tile:  # Check if the tile is valid
                            self.screen.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))    