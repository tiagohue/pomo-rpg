from gamification import load_data
from ui.screens.search_for_monsters_screen import search_for_monsters_screen
from ui.utils import clear_terminal, display_status


def time_tower_menu():
    print("Time Tower Menu:")
    print("1 - Search for Monsters")
    print("2 - Exit")
    return input()

def time_tower_screen():
    while True:
        clear_terminal()
        display_status(load_data())
        answer = time_tower_menu()
        match answer:
            case "1":
                search_for_monsters_screen()
            case "2":
                break
            case _:
                input("Please select a valid option!")