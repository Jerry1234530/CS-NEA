from settings import *  # Assuming the constants (TILE_ROWS, TILE_COLS, etc.) are in the settings file.
import pygame

class Tile:
    def __init__(self, x, y, width, height, row, col):
        self.rect = pygame.Rect(x, y, width, height)
        self.crop = None # No crop by default
        self.selected = False  # Track if the tile is selected
        self.row = row  # Row index of the tile
        self.col = col  # Column index of the tile
        self.progress = 0 # Progress of the planted crop 
        self.value = 0 


    def __str__(self):
        # Return the string representation of the tile's relative position (row, col)
        crop_info = f"Crop: {self.crop if self.crop else 'None'}"
        progress_info = f"Progress: {50 if self.crop else 0}%"
        value_info = f"Value: £20"  # Assuming a fixed value for now
        position_info = f"Position: ({self.row + 1}, {self.col + 1})"  # 1-based indexing
        return f"Tile {position_info} - {crop_info}, {progress_info}, {value_info}"

    def draw(self, screen):
        if self.crop is None:
            pygame.draw.rect(screen, WHITE, self.rect)  # Empty tile
        else:
            pygame.draw.rect(screen, GREEN, self.rect)  # Tile with crop
        if self.selected:
            pygame.draw.rect(screen, BLUE, self.rect, 3)  # Highlight selected tile
        pygame.draw.rect(screen, GREEN, self.rect, 1)  # Tile border

    
    def update(self):
        if self.crop is not None:  # Only progress if there is a crop
            self.progress += 0.05  # Increment progress

            if self.progress >= 100:
                self.progress = 100  # Cap the progress at 100% but don't reset crop
                # Optionally, you can add some other logic for when the crop is ready for harvest



class Grid:
    def __init__(self, screen):
        self.rows = TILE_ROWS
        self.cols = TILE_COLS
        self.tile_width = TILE_WIDTH
        self.tile_height = TILE_HEIGHT
        self.screen = screen
        self.tiles = self.create_tiles()

    def create_tiles(self):
        tiles = []
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.tile_width
                y = row * self.tile_height
                tile = Tile(x, y, self.tile_width, self.tile_height, row, col)  # Pass row and col
                tiles.append(tile)
        return tiles

    def draw(self):
        for tile in self.tiles:
            tile.draw(self.screen)

    def get_tile_at_pos(self, mouse_pos):
        for tile in self.tiles:
            if tile.rect.collidepoint(mouse_pos):
                return tile  # Return the clicked tile
        return None  # If no tile is clicked   
    
    def update(self): 
        for tile in self.tiles: 
            tile.update() 
