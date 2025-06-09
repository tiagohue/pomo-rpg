from data.repository import get_random_enemy
from ui.components import clear_terminal, display_status

def display_monster():
    enemy = get_random_enemy()
    print(f"You found a {enemy["name"]}!")
    

def display_combat_menu():
    print("Combat Menu:")
    print("1 - Attack enemy")
    print("2 - Escape")
    return input()

def combat_screen():
    clear_terminal()
    display_status()
    display_monster()
    display_combat_menu()
