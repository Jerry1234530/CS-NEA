import pygame 
from settings import * 

class Sidebar: 
    def __init__(self, screen): 
        self.width = SIDEBAR_WIDTH
        self.height = SCREEN_HEIGHT 
        self.screen = screen
        self.pos = (SCREEN_WIDTH - SIDEBAR_WIDTH, 0 ) 
        self.selected_tile = None
        self.font = pygame.font.Font(None , 36)

    def update(self, selected_tile): 
        self.selected_tile = selected_tile 
    
    def draw(self): 
        pygame.draw.rect(self.screen, BLACK, (*self.pos, self.width, self.height))

        if self.selected_tile: 
            tile_info = [
                f"Tile Position: ({self.selected_tile.row + 1}, {self.selected_tile.col + 1})",  # 1-based indexing
                f"Crop: {self.selected_tile.crop if self.selected_tile.crop else 'None'}",
                f"Progress: {int(self.selected_tile.progress)}%",  # Example progress
                f"Value: {self.selected_tile.value}"  # Placeholder value
            ]
        
            for i, line in enumerate(tile_info): 
                text_surface = self.font.render(line, True, WHITE) 
                self.screen.blit(text_surface, (self.pos[0] + 10, self.pos[1] + 10 + i * 30))
            
            # Draw the sell button
            sell_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 150, 100, 40) 
            pygame.draw.rect(self.screen, (150, 0, 0), sell_button_rect) 
            sell_text = self.font.render("Sell", True, WHITE) 
            self.screen.blit(sell_text, (sell_button_rect.x + 20, sell_button_rect.y + 10 ))

            # Draw the Plant Wheat button
            plant_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 200, 250, 40) 
            pygame.draw.rect(self.screen , (0, 150, 0), plant_button_rect) 
            plant_text = self.font.render("Plant Wheat (£5)", True, WHITE) 
            self.screen.blit(plant_text, (plant_button_rect.x + 10, plant_button_rect.y + 10))

            #Draw the 



    def check_sell_button(self, mouse_pos): 
        if self.selected_tile.progress == 100: 
            sell_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 150, 100, 40) 
            return sell_button_rect.collidepoint(mouse_pos)  # Check if mouse is over the sell button
        else:
            return False 

    def check_plant_button(self, mouse_pos): 
        plant_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 200, 250, 40) 
        return plant_button_rect.collidepoint(mouse_pos)  # Check if mouse is over the plant button 

