from gamification import load_data
from ui.utils import clear_terminal, display_status

def display_monster():
    print("You found a slime!")
    input("todo")

def search_for_monsters_screen():
    clear_terminal()
    display_status(load_data())
    display_monster()
