# Computer Science NEA – Python Farming Game

A tile-based farming simulator developed using **Python and Pygame** for my A Level Computer Science NEA project.

---

## Gameplay Overview

Plant crops, earn money, and manage your rent before the timer runs out! Each crop grows over time and can be sold for profit. A recurring **rent timer** forces you to balance growth and income strategically.

---

## Rent System
- Initial rent: £100
- Every rental cycle increases rent by £100
- If you can't pay, the game ends
- You can **disable rent** in the Options menu

---

## 🖥The Sidebar
Displays details for the currently selected tile:
- **Tile Position** – Coordinates of the selected tile (e.g., (1, 3))
- **Crop** – Type of crop planted
- **Progress** – Growth percentage (0%–100%)
- **Value** – Sell value of the crop
- **Rent Timer** – Time remaining before rent is due
- **Sell** – Button to sell the crop (must be fully grown)
- **Plant** – Buttons to plant Wheat, Cotton, Oat, or Melon (if tile is empty and you have enough money)

---

## Controls

**Mouse**:  
- Click tiles to select  
- Click sidebar buttons to plant or sell crops

**Keyboard**:  
- Use arrow keys to move between tiles

---

## Running the Game

1. Make sure Python 3.x is installed
2. Install Pygame:
   ```bash
   pip install pygame

