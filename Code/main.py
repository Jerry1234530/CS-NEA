import pygame , sys
from settings import * 
from level import Level 
import pytmx
class Game: 
    def __init__(self): 
        pygame.init() 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Farming NEA Project')
        self.clock = pygame.time.Clock() 
        self.level = Level()     

    def run(self): 
        while True: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit() 
            
            deltatime = self.clock.tick() / 1000 
            self.level.run(deltatime) 
            pygame.display.update() 

    def draw_map(self): 
            for layer in self.tmx_data.visible_layers:
                if isinstance(layer, pytmx.TiledTileLayer): 
                    for x , y, gid in layer: 
                        tile = self.tmx_data.get_tile_image_by_grid(gid) 
                        if tile:
                            self.screen.blit(tile,(x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))
if __name__ == '__main__'   : 
    game = Game() 
    game.run() 
