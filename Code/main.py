#---------IMPORTS---------#
import pygame
import sys
from settings import *
from button import Button
from grid import Grid
from grid import Tile
from sidebar import Sidebar
from upgrades import Upgrades
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
        upg = Upgrades() 
        rent_interval = 100000
        last_rent_time = pygame.time.get_ticks() 
        rent_cost = 200
        while True:
            current_time = pygame.time.get_ticks()
            time_to_next_rent = max(0, (last_rent_time + rent_interval - current_time)) / 1000
            
            if current_time - last_rent_time >= rent_interval:
                if self.money >= 200: 
                    self.money -= rent_cost 
                    print(f"Rent Charged: {rent_cost}.")
                    rent_cost += 100

                else: 
                    print(f"Not enough money to rent. You Lose") 
                    self.main_menu()
                last_rent_time = current_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


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
                            print(f"Sold crop from Tile {self.selected_tile}")
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
                            print("Not enough money to plant a crop OR crop already exists") 
                    if sidebar.check_cotton_pant_button(mouse_pos): 
                        if self.selected_tile and self.money >= 10 and self.selected_tile.crop is None: 
                            print(f"DEBUG: Planted crop on Tile {self.selected_tile}")
                            print("DEBUG: Took £10 from balance") 
                            self.money -= 10  # Decrease the player's balance
                            self.selected_tile.crop = "Cotton Plant"   # Place a crop on the selected tile
                            self.selected_tile.value = 30 
                            sidebar.update(self.selected_tile)  # Update the sidebar to reflect the planting
                        else: 
                            print("Not enough money to plant a crop OR crop already exists")
                    if sidebar.check_oat_plant_button(mouse_pos): 
                        if self.selected_tile and self.money >= 15 and self.selected_tile.crop is None: 
                            print(f"DEBUG: Planted crop on Tile {self.selected_tile}")
                            self.money -= 15  # Decrease the player's balance
                            self.selected_tile.crop = "Oat Plant"   # Place a crop on the selected tile
                            self.selected_tile.value = 40 
                            sidebar.update(self.selected_tile)  # Update the sidebar to reflect the planting
                        else: 
                            print("Not enough money to plant a crop OR crop already exists")

                        

            # Clear the screen and draw the grid, sidebar, and selected tile
            self.screen.fill(WHITE)
            grid.draw()  # Draw the grid with tiles
            sidebar.draw(time_to_next_rent , self.money , rent_cost)  # Draw the sidebar with the selected tile info
            money_text = self.font.render(f"Money: £{self.money}", True, GREEN)
            rent_text = self.font.render(f"Rent: £{rent_cost}", True, RED) 
            pygame.display.set_caption(f"Money: {self.money} Farming Game ")
            self.screen.blit(money_text, (980, 670))  # Display the player's money on the screen
            grid.update() 
            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit the frame rate to 60 FPS
        
    def options(self):
    # Set up a timer to display the message
        start_time = pygame.time.get_ticks()  # Get the current time in milliseconds
        display_message = True

        while display_message:
            self.screen.fill(WHITE)  # Clear the screen
            options_text = self.font.render("Options will be added soon", True, GREEN)
            options_rect = options_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(options_text, options_rect)

            pygame.display.flip()  # Update the display

            # Check if 3 seconds have passed
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 3000:  # 3000 ms = 3 seconds
                display_message = False

            # Handle events to allow quitting or skipping
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # After the message, return to the main menu
        self.main_menu()#
    
    def game_over(self): 
        pass

if __name__ == '__main__':
    game = Game()
    game.main_menu()
