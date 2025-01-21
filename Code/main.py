#---------IMPORTS---------#
import pygame
import sys
from settings import *
from button import Button
from grid import Grid
from grid import Tile
from sidebar import Sidebar
#---------IMPORTS---------#


#---------Game Class---------#
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Farming NEA Project')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 36)
        self.BG = pygame.image.load('./Assets/background.png')
        self.selected_tile = None  # Track the selected tile
        self.money = 5 # Set the money 
        self.rent_enabled = True #Default: True. 

    def main_menu(self):
        pygame.display.set_caption("Main Menu : Farming Game")
        while True:
            self.screen.blit(self.BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.font.render("MAIN MENU", True, GREEN)
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("./Assets/Play Rect.png"), pos=(640, 250),
                                 text_input='PLAY', font=self.font, base_color=ORANGE, hovering_color='WHITE')
            OPTIONS_BUTTON = Button(image=pygame.image.load("./Assets/Options Rect.png"), pos=(640, 400),
                                    text_input='OPTIONS', font=self.font, base_color=ORANGE, hovering_color='WHITE')
            QUIT_BUTTON = Button(image=pygame.image.load("./Assets/Quit Rect.png"), pos=(640, 550),
                                 text_input='QUIT', font=self.font, base_color=ORANGE, hovering_color='WHITE')

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.CheckForInput(MENU_MOUSE_POS):
                        self.play()
                        print("DEBUG: PLAY")
                    if OPTIONS_BUTTON.CheckForInput(MENU_MOUSE_POS):
                        self.options() 
                    if QUIT_BUTTON.CheckForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def play(self):
        # Initialize the grid and sidebar
        grid = Grid(self.screen)
        print ("Loaded Grid")
        sidebar = Sidebar(self.screen)
        print ("Loaded Sidebar")
        self.selected_tile = None  # Reset the selected tile when the game starts        
        pygame.mixer.init() 
        rent_interval = 100000
        last_rent_time = pygame.time.get_ticks() 
        rent_cost = 100
        while True:
            current_time = pygame.time.get_ticks()
            time_to_next_rent = max(0, (last_rent_time + rent_interval - current_time)) / 1000


            if current_time - last_rent_time >= rent_interval and self.rent_enabled: #Checks if rent is enabled and that the rent is due.
                if self.money >= rent_cost: 
                    self.money -= rent_cost 
                    print(f"Rent Charged: {rent_cost}.")
                    rent_cost += 100

                else: 
                    print(f"Not enough money to rent. You Lose!") 
                    self.money = 5 
                    self.game_over() 
                last_rent_time = current_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if self.selected_tile:  # Check if a tile is selected
                        row, col = self.selected_tile.row, self.selected_tile.col
                        if event.key == pygame.K_UP and row > 0:
                            self.selected_tile.selected = False
                            self.selected_tile = grid.tiles[(row - 1) * TILE_COLS + col]
                        elif event.key == pygame.K_DOWN and row < TILE_ROWS - 1:
                            self.selected_tile.selected = False
                            self.selected_tile = grid.tiles[(row + 1) * TILE_COLS + col]
                        elif event.key == pygame.K_LEFT and col > 0:
                            self.selected_tile.selected = False
                            self.selected_tile = grid.tiles[row * TILE_COLS + (col - 1)]
                        elif event.key == pygame.K_RIGHT and col < TILE_COLS - 1:
                            self.selected_tile.selected = False
                            self.selected_tile = grid.tiles[row * TILE_COLS + (col + 1)]

                        self.selected_tile.selected = True
                        sidebar.update(self.selected_tile)  # Update the sidebar

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    # Handle tile selection
                    clicked_tile = grid.get_tile_at_pos(mouse_pos)
                    if clicked_tile:
                        if self.selected_tile:
                            self.selected_tile.selected = False  # Deselect the previous tile
                        clicked_tile.selected = True  # Select the new tile
                        self.selected_tile = clicked_tile # Update the selected tile

                        # Update sidebar based on the selected tile
                        sidebar.update(self.selected_tile)

                    # Handle sell button in sidebar
                    if sidebar.check_sell_button(mouse_pos):
                        if self.selected_tile:
                            print(f"DEBUG: Sold crop from {self.selected_tile}")
                            self.money += self.selected_tile.value 
                            self.selected_tile.progress = 0
                            self.selected_tile.crop = None  # Remove the crop from the selected tile
                            self.selected_tile.value = 0 
                            sidebar.update(self.selected_tile)  # Update the sidebar to reflect no selection

                    if sidebar.check_plant_button(mouse_pos): 
                        if self.selected_tile and self.money >= 5 and self.selected_tile.crop is None: 
                            print(f"DEBUG: Planted crop on Tile {self.selected_tile}")
                            self.money -= 5  # Decrease the player's balance
                            self.selected_tile.crop = "Wheat"   # Place a crop on the selected tile
                            self.selected_tile.value = 20 
                            sidebar.update(self.selected_tile)  # Update the sidebar to reflect the planting
                        else: 
                            print("DEBUG: Not enough money to plant a crop OR crop already exists") 
                    if sidebar.check_cotton_pant_button(mouse_pos): 
                        if self.selected_tile and self.money >= 10 and self.selected_tile.crop is None: 
                            print(f"DEBUG: Planted crop on Tile {self.selected_tile}")
                            print("DEBUG: Took £10 from balance") 
                            self.money -= 10  # Decrease the player's balance
                            self.selected_tile.crop = "Cotton Plant"   # Place a crop on the selected tile
                            self.selected_tile.value = 30 
                            sidebar.update(self.selected_tile)  # Update the sidebar to reflect the planting
                        else: 
                            print("DEBUG: Not enough money to plant a crop OR crop already exists")
                    if sidebar.check_oat_plant_button(mouse_pos): 
                        if self.selected_tile and self.money >= 15 and self.selected_tile.crop is None: 
                            print(f"DEBUG: Planted crop on Tile {self.selected_tile}")
                            self.money -= 15  # Decrease the player's balance
                            self.selected_tile.crop = "Oat Plant"   # Place a crop on the selected tile
                            self.selected_tile.value = 40 
                            sidebar.update(self.selected_tile)  # Update the sidebar to reflect the planting
                        else: 
                            print("DEBUG: Not enough money to plant a crop OR crop already exists")
                    if sidebar.check_millet_plant_button(mouse_pos): 
                        pass 

                        

            # Clear the screen and draw the grid, sidebar, and selected tile
            self.screen.fill(WHITE)
            grid.draw()  # Draw the grid with tiles
            sidebar.draw(time_to_next_rent , self.money , rent_cost, self.rent_enabled)  # Draw the sidebar with the selected tile info
            money_text = self.font.render(f"Money: £{self.money}", True, GREEN)
            rent_text = self.font.render(f"Rent: £{rent_cost}", True, RED) 
            pygame.display.set_caption(f"Money: {self.money} Farming Game ")
            self.screen.blit(money_text, (980, 670))  # Display the player's money on the screen
            grid.update() 
            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit the frame rate to 60 FPS
        
    def options(self):
        display_message = True 

        while display_message: 
            self.screen.fill(WHITE) 

            #Options Text 
            option_text = self.font.render("OPTIONS MENU", True , GREEN)
            options_rect = option_text.get_rect(center=(SCREEN_WIDTH // 2 , 100)) 
            self.screen.blit(option_text, options_rect)

            # Rent Toggle Button
            toggle_text = "Disable Rent" if self.rent_enabled else "Enabled Rent"
            TOGGLE_BUTTON = Button(image = pygame.image.load("./Assets/Options Rect.png"), pos=(640,250), 
                                    text_input = toggle_text, font = self.font, base_color=ORANGE, hovering_color='WHITE')

            #Return to main menu button
            RETURN_BUTTON = Button(image=pygame.image.load("./Assets/Quit Rect.png"), pos=(640, 400),
                                   text_input= "Return to Main Menu", font = self.font, base_color=ORANGE, hovering_color = WHITE) 
            
            #Render Buttons
            TOGGLE_BUTTON.update(self.screen)
            RETURN_BUTTON.update(self.screen) 

            pygame.display.flip() 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos() 

                    if TOGGLE_BUTTON.CheckForInput(mouse_pos): 
                        self.rent_enabled = not self.rent_enabled
                        toggle_text = "Disable Rent" if self.rent_enabled else "Enable Rent" 
                    
                    if RETURN_BUTTON.CheckForInput(mouse_pos):  
                        self.main_menu() 

                    
    def game_over(self): 
        display_message = True 
        mouse_pos = pygame.mouse.get_pos() 
        while display_message: 
            self.screen.fill(WHITE) 
 
                
            #Game Over Text
            game_over_text = self.font.render("GAME OVER", True , GREEN)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2 , 100)) 
            self.screen.blit(game_over_text, game_over_rect) 
            
            #Return to main menu button 
            RETURN_BUTTON = Button(image=pygame.image.load("./Assets/Quit Rect.png"), pos=(640, 400),
                                   text_input= "Return to Main Menu", font = self.font, base_color=ORANGE, hovering_color = WHITE) 
            
            #Return to Game Menu Button
            GAME_BUTTON = Button(image=pygame.image.load("./Assets/Quit Rect.png"),pos= (640, 600), 
                                 text_input= "Return to Game", font = self.font , base_color=ORANGE, hovering_color = WHITE) 
            
            #Render Buttons
            RETURN_BUTTON.update(self.screen) 
            GAME_BUTTON.update(self.screen) 


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos() 
                    
                    if RETURN_BUTTON.CheckForInput(mouse_pos): 
                        self.main_menu() 
                    
                    if GAME_BUTTON.CheckForInput(mouse_pos): 
                        self.play() 

            pygame.display.flip() 

        

if __name__ == '__main__':
    game = Game()
    game.main_menu()
