import pygame
import sys
from settings import *
from tile import TiledMap
import pytmx
from pytmx import load_pygame
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Farming NEA Project')
        self.clock = pygame.time.Clock()
        self.tmx_data = load_pygame('./Assets/tmx/untitled.tmx')  # Ensure the path is correct
        self.level = Level() 
        self.all_sprites = pygame.sprite.Sprite() 
        self.tile = TiledMap((1,1), self.screen, self.all_sprites) 

    def run(self):
        """
        Main game loop.
        """ 
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear the screen
            self.screen.fill((0, 0, 0))
            self.tile.draw(self.all_sprites) 

            # Run game level logic
            deltatime = self.clock.tick(60) / 1000  # Cap frame rate to 60 FPS
            self.level.run(deltatime)

            # Update the display
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
