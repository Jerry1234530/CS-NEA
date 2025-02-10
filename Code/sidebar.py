import pygame 
from settings import * 
#Import End
class Sidebar: 
    def __init__(self, screen): 
        self.width = SIDEBAR_WIDTH
        self.height = SCREEN_HEIGHT 
        self.screen = screen
        self.pos = (SCREEN_WIDTH - SIDEBAR_WIDTH, 0 ) 
        self.selected_tile = None
        self.font = pygame.font.Font(None , 36)

    def update(self, selected_tile): 
        self.selected_tile = selected_tile #Checks that the selected tile hasn't been changed 
    
    def draw(self ,time_to_next_rent, money , rent_cost , rent_enabled): 
        pygame.draw.rect(self.screen, BLACK, (*self.pos, self.width, self.height))

        if self.selected_tile: 
            tile_info = [
                f"Tile Position: ({self.selected_tile.row + 1}, {self.selected_tile.col + 1})",  #Displays the coordinates of the tile
                f"Crop: {self.selected_tile.crop if self.selected_tile.crop else 'None'}", #Shows the name of the crop within the tile. 
                f"Progress: {int(self.selected_tile.progress)}%",  #Gets the progress of the selected tile 
                f"Value: {self.selected_tile.value}"  #Gets the value of the value of the selected tile 
            ]
        
            for i, line in enumerate(tile_info): 
                text_surface = self.font.render(line, True, WHITE) 
                self.screen.blit(text_surface, (self.pos[0] + 10, self.pos[1] + 10 + i * 30))
            

            #Display Rent Timer
            if money < rent_cost and rent_enabled is True:
                rent_text = self.font.render(f"Rent Timer: {time_to_next_rent}s ", True, RED)
                self.screen.blit(rent_text, (self.pos[0] + 10, self.pos[1] + 125))
            else: #The code above is the same throughout the rent timer but only with different conditions.
                  # It works by blitting the text and button to the screen. 
                if rent_enabled is True: 
                    rent_text = self.font.render(f"Rent Timer: {time_to_next_rent}s ", True, GREEN)
                    self.screen.blit(rent_text, (self.pos[0] + 10, self.pos[1] + 125))
            
            if rent_enabled is False: 
                rent_text = self.font.render("Rent Disabled", True, GREEN)
                self.screen.blit(rent_text, (self.pos[0] + 10, self.pos[1] + 125)) 
            
            # Draw the sell button
            sell_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 150, 100, 40) 
            pygame.draw.rect(self.screen, (150, 0, 0), sell_button_rect) 
            sell_text = self.font.render("Sell", True, WHITE) 
            self.screen.blit(sell_text, (sell_button_rect.x + 20, sell_button_rect.y + 10 ))

            # Draw the Plant Wheat button
            plant_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 200, 250, 40) 
            pygame.draw.rect(self.screen , (0, 150, 0), plant_button_rect) 
            plant_text = self.font.render("Plant Wheat (£5)", True, WHITE) #Shows what the plant button text will display 
            self.screen.blit(plant_text, (plant_button_rect.x + 10, plant_button_rect.y + 10))

            #Draw the Plant Cotton Button
            cotton_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 250 , 250 , 40)
            pygame.draw.rect(self.screen, (0, 150, 0), cotton_button_rect) 
            cotton_text = self.font.render("Plant Cotton (£10)", True, WHITE)
            self.screen.blit(cotton_text, (cotton_button_rect.x + 10, cotton_button_rect.y + 10))
            #Draw the Plant Oat Button
            oat_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 300, 250, 40)
            pygame.draw.rect(self.screen, (0, 150, 0), oat_button_rect) 
            oat_text = self.font.render("Plant Oat (£15)", True, WHITE)
            self.screen.blit(oat_text, (oat_button_rect.x + 10, oat_button_rect.y + 10))

#The buttons all above are reusable code components and all work by changing where the button is positioned and what the cost to plant the button is. 


    def check_sell_button(self, mouse_pos): 
        if self.selected_tile.progress == 100: 
            sell_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 150, 100, 40) #Sets the location of the plant button  
            return sell_button_rect.collidepoint(mouse_pos)  # Check if mouse is over the sell button


    def check_plant_button(self, mouse_pos): 
        plant_button_rect = pygame.Rect(self.pos[0] + 10 , self.pos[1] + 200, 250, 40) #Sets the location of the plant button 
        return plant_button_rect.collidepoint(mouse_pos)  # Check if mouse is over the plant button 

    def check_cotton_pant_button(self, mouse_pos): 
        plant_button_rect = pygame.Rect(self.pos[0] + 10, self.pos[1] + 250 , 250 , 40) #Sets the location of the plant button
        return plant_button_rect.collidepoint(mouse_pos)  # Check if mouse is over the plant button
    
    def check_oat_plant_button(self, mouse_pos):
        plant_button_rect = pygame.Rect(self.pos[0] + 10, self.pos[1] + 300, 250, 40)   #Sets the location of the plant button
        return plant_button_rect.collidepoint(mouse_pos)  # Check if mouse is over the plant button
        
#Again an example of reusable elements of code within the program. There is nothing uniquely special about each check just the area in which it is 
#checking where the mouse is positioned. 
